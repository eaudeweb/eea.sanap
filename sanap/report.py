import xlsxwriter

from collections import OrderedDict
from StringIO import StringIO

from flask import views
from flask import Blueprint
from flask.ext import login as flask_login
from flask import send_file

from sanap import models
from sanap import forms
from sanap.model_data import *
from sanap.auth import login_required, eea_admin


report = Blueprint('report', __name__)


FIELDS = ('public_awareness', 'adaptation_need', 'triggers', 'willingness',
          'knowledge', 'uncertainties', 'objectives', 'integration', 'mitigation',
          'transnational_cooperation', 'barriers', 'process_stage',
          'horizontal_integration', 'vertical_integration', 'assessment',
          'assessment_scale', 'sectors_assessments', 'needed_info',
          'assessment_update', 'adaptation_options', 'adaptation_scale', 'identified_options',
          'adaptation_actions', 'prioritised_options', 'monitoring_state', 'reporting_state',
          'evaluation_state', 'sectors', 'instruments', 'main_instruments', 'financing_mechanisms',
          'stakeholders_involved', 'stakeholders_contribution',
          'development_involvement', 'implementation_involvement', 'monitoring_involvement',)


SIMPLE_FIELDS_CHOICES = {
    'public_awareness': AGREEMENT_DATA,
    'adaptation_need': AGREEMENT_DATA,
    'triggers': TRIGGER_DATA,
    'willingness': LEVEL_DATA,
    'knowledge': AGREEMENT_DATA,
    'uncertainties': AGREEMENT_DATA,
    'objectives': AGREEMENT_DATA,
    'integration': AGREEMENT_DATA,
    'mitigation': AGREEMENT_DATA,
    'transnational_cooperation': AGREEMENT_DATA,
    'barriers': BARRIER_DATA,
    'process_stage': PROCESS_STAGE_DATA,
    'horizontal_integration': EFFECTIVENESS_DATA,
    'vertical_integration': EFFECTIVENESS_DATA,
    'assessment': STATUS_DATA,
    'assessment_scale': ASSESSMENT_SCALE_DATA,
    'needed_info': NEEDED_INFO_DATA,
    'assessment_update': PLANNING_DATA,
    'adaptation_options': STATUS_DATA,
    'adaptation_scale': ADAPTATION_SCALE_DATA,
    'identified_options': IDENTIFIED_OPTIONS_DATA,
    'adaptation_actions': ADAPTATION_ACTIONS_DATA,
    'prioritised_options': STATUS_DATA,
    'monitoring_state': STATE_OF_WORK_DATA,
    'reporting_state': STATE_OF_WORK_DATA,
    'evaluation_state': STATE_OF_WORK_DATA,
    'instruments': INSTRUMENTS_DATA,
    'stakeholders_involved': YES_NO_DATA,
    'stakeholders_contribution': STAKEHOLDERS_CONTRIBUTION_DATA,
}


MATRIX_FIELDS = ('sectors_assessments', 'main_instruments', 'financing_mechanisms',
                 'development_involvement', 'implementation_involvement',
                 'monitoring_involvement', 'sectors')


MATRIX_FIELDS_FORMS = {
    'sectors_assessments': forms.SectorsAssessmentsForm,
    'main_instruments': forms.MainInstrumentsForm,
    'financing_mechanisms': forms.MainInstrumentsForm,
    'development_involvement': forms.InvolmentForm,
    'implementation_involvement': forms.InvolmentForm,
    'monitoring_involvement': forms.InvolmentForm,
    'sectors': forms.SectorsForm,
}


MATRIX_FIELDS_CHOICES = {
    'sectors_assessments': SECTORS_DATA,
    'main_instruments': MAIN_INSTRUMENTS_DATA,
    'financing_mechanisms': FINANCING_MECHANISMS_DATA,
    'development_involvement': INVOLVEMENT_DATA,
    'implementation_involvement': INVOLVEMENT_DATA,
    'monitoring_involvement': INVOLVEMENT_DATA,
    'sectors': SECTORS_DATA,
}


def initialize_app(app):
    app.register_blueprint(report)


def clean_label(label):
    label = label.replace('<b>', '').replace('</b>', '')
    label = label.replace('<strong>', '').replace('</strong>', '')
    return label


def add_count(stats, field_name, value):
    stats.setdefault(field_name, OrderedDict())
    for choice in SIMPLE_FIELDS_CHOICES.get(field_name, []):
        stats[field_name].setdefault(choice, 0)
    if value in stats[field_name]:
        stats[field_name][value] += 1
    else:
        stats[field_name][value] = 1
    return stats


def add_dict_count(stats, field_name, dex):
    if not bool([item for sublist in dex.values() for item in sublist]):
        return

    stats.setdefault(field_name, OrderedDict())
    if stats[field_name].items():
        matrix_data = stats[field_name]
    else:
        matrix_data = OrderedDict()

    column_keys = [(i.id, clean_label(i.label.text)) for i in MATRIX_FIELDS_FORMS[field_name]()
                   if i.id != 'csrf_token']

    for key in MATRIX_FIELDS_CHOICES[field_name]:
        for col in column_keys:
            matrix_data.setdefault(key, OrderedDict())
            if not col[0] in matrix_data[key]:
                matrix_data[key][col[0]] = 0

    for key, items in dex.items():
        for item in items:
            matrix_data.setdefault(item, OrderedDict())
            if not key in matrix_data[item]:
                for col in column_keys:
                    matrix_data[item][col[0]] = 0
            matrix_data[item][key] += 1

    matrix = [('',) + tuple(map(lambda x: x[1], column_keys))]
    for key, values in matrix_data.items():
        matrix.append((key,) + tuple(map(lambda x: x[1], values.items())))

    stats[field_name] = matrix_data
    stats[field_name + '_matrix'] = matrix
    return stats


def process_stats():
    stats = OrderedDict()
    for field_name in FIELDS:
        stats[field_name] = OrderedDict()

    for survey in models.Survey.objects.filter(for_eea=True, draft=False):
        for field_name in FIELDS:
            value = getattr(survey, field_name, None)
            if not value:
                continue
            if isinstance(value, basestring):
                add_count(stats, field_name, value)
            if isinstance(value, list):
                for item in value:
                  add_count(stats, field_name, item)
            if isinstance(value, dict):
                add_dict_count(stats, field_name, value)
    return stats


class Report(views.MethodView):

    decorators = (login_required, eea_admin)

    def get(self):
        stats = process_stats()
        form = forms.SurveyForm()
        output = StringIO()

        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        row = 0
        for field, answers in stats.items():
            if 'matrix' in field:
                continue

            if field == 'development_involvement':
                worksheet.write(row, 0, clean_label(Q['40']))
                row += 2

            question = getattr(form, field, None)
            worksheet.write(row, 0, clean_label(question.label.text))

            row += 1
            if field in MATRIX_FIELDS:
                for answer in stats[field + '_matrix']:
                    for i, item in enumerate(answer):
                        worksheet.write(row, i, item)
                    row += 1
            else:
                for answer, count in answers.items():
                    worksheet.write(row, 0, answer)
                    worksheet.write(row, 1, count)
                    row += 1
            row += 3

        workbook.close()
        output.seek(0)
        return send_file(output, attachment_filename='report.xlsx',
                         as_attachment=True)

report.add_url_rule('/report', view_func=Report.as_view('report'))
