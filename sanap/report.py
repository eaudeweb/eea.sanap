import xlsxwriter

from collections import OrderedDict
from StringIO import StringIO

from flask import views
from flask import Blueprint
from flask.ext import login as flask_login
from flask import send_file

from sanap import models
from sanap.forms import SurveyForm


report = Blueprint('report', __name__)


FIELDS = ('public_awareness', 'adaptation_need', 'triggers', 'willingness',
          'knowledge', 'uncertainties', 'objectives', 'integration', 'mitigation',
          'transnational_cooperation', 'barriers', 'process_stage',
          'horizontal_integration', 'vertical_integration',)


def initialize_app(app):
    app.register_blueprint(report)


def add_count(stats, field_name, value):
    if not field_name in stats:
        stats.setdefault(field_name, OrderedDict())
    if value in stats[field_name]:
        stats[field_name][value] += 1
    else:
        stats[field_name][value] = 1
    return stats


def process_stats():
    stats = OrderedDict()
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
    return stats


class Report(views.MethodView):

    @flask_login.login_required
    def get(self):
        stats = process_stats()
        form = SurveyForm()
        output = StringIO()

        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        row = 0
        for field, answers in stats.items():
            question = getattr(form, field, None)
            worksheet.write(row, 0, question.label.text)

            row += 1

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
