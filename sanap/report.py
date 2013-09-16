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


def add_dict_count(stats, field_name, dex, columns=[]):
    if not bool([item for sublist in dex.values() for item in sublist]):
        return

    stats.setdefault(field_name, OrderedDict())
    if stats[field_name].items():
        matrix_data = stats[field_name]
    else:
        matrix_data = OrderedDict()

    column_keys = [(i.id, clean_label(i.label.text)) for i in MATRIX_FIELDS_FORMS[field_name]()
                   if i.id != 'csrf_token']
    if columns:
        column_keys = [i for i in column_keys if i[0] in columns]

    for key in MATRIX_FIELDS_CHOICES[field_name]:
        for col in column_keys:
            matrix_data.setdefault(key, OrderedDict())
            if not col[0] in matrix_data[key]:
                matrix_data[key][col[0]] = 0

    for key, items in dex.items():
        if columns and key not in columns:
            continue
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


def add_sectors_count(stats, field_name, dex):
    stats.setdefault(field_name, OrderedDict())

    column_keys = [(i.id, clean_label(i.label.text)) for i in MATRIX_FIELDS_FORMS[field_name]()
                   if i.id != 'csrf_token'][:3]
    choices = [i for i in MATRIX_FIELDS_CHOICES[field_name]]

    if stats[field_name].items():
        matrix_data = stats[field_name]
    else:
        matrix_data = OrderedDict()

    for key in column_keys:
        matrix_data.setdefault(key[0], OrderedDict())

    for data in matrix_data:
        for choice in choices:
            matrix_data[data].setdefault(choice, OrderedDict([
                ('0-1', 0),
                ('2-3', 0),
                ('4-5-6', 0),
            ]))

    for key, items in dex.items():
        if key not in [c[0] for c in column_keys]:
            continue
        for item, count in items.items():
            try:
                count = int(count)
            except ValueError:
                count = 0
            if int(count) in range(0, 2):
                matrix_data[key][item]['0-1'] += 1
            if int(count) in range(2, 4):
                matrix_data[key][item]['2-3'] += 1
            if int(count) in range(4, 6):
                matrix_data[key][item]['4-5-6'] += 1

    matrix_data_2 = OrderedDict()
    for choice in choices:
        matrix_data_2[choice] = OrderedDict()

    for data in matrix_data_2:
        for col in column_keys:
            matrix_data_2[data].setdefault(col[0], OrderedDict([
                ('0-1', 0),
                ('2-3', 0),
                ('4-5-6', 0),
            ]))

    for key, items in matrix_data.items():
        for choice, values in items.items():
            matrix_data_2[choice][key]['0-1'] = values['0-1']
            matrix_data_2[choice][key]['2-3'] = values['2-3']
            matrix_data_2[choice][key]['4-5-6'] = values['4-5-6']

    matrix = []
    for key, items in matrix_data.items():
        matrix.append((dict(column_keys)[key], '', '', ''))
        matrix.append(('', '0-1', '2-3', '4-5-6'))
        for choice, values in items.items():
            matrix.append((choice,) + tuple(values.values()))
        matrix.append(('', '', '', ''))
    matrix.append(('', '', '', ''))
    matrix.append(('', '', '', ''))

    for key, items in matrix_data_2.items():
        matrix.append((key, '', '', ''))
        matrix.append(('', '0-1', '2-3', '4-5-6'))
        for choice, values in items.items():
            matrix.append((dict(column_keys)[choice],) + tuple(values.values()))
        matrix.append(('', '', '', ''))

    stats[field_name] = matrix_data
    stats[field_name + '_matrix'] = matrix

    return stats


def process_stats():
    stats = OrderedDict()
    sectors_stats = OrderedDict()

    for field_name in FIELDS:
        stats[field_name] = OrderedDict()

    for survey in models.Survey.objects.filter(for_eea=True, draft=False):
        for field_name in FIELDS:
            value = getattr(survey, field_name, None)
            if not value:
                continue
            if field_name == 'sectors':
                add_sectors_count(stats, field_name, value)
                add_dict_count(sectors_stats, field_name, value,
                               columns='priority_sectors')
                continue
            if isinstance(value, basestring):
                add_count(stats, field_name, value)
            if isinstance(value, list):
                for item in value:
                  add_count(stats, field_name, item)
            if isinstance(value, dict):
                add_dict_count(stats, field_name, value)
    return (stats, sectors_stats)


class Report(views.MethodView):

    decorators = (login_required, eea_admin)

    def get(self):
        stats, sectors_stats = process_stats()
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

            if field == 'sectors':
                for answer in sectors_stats[field + '_matrix']:
                    for i, item in enumerate(answer):
                        worksheet.write(row, i, item)
                    row += 1
                row += 1

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
