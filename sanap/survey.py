import subprocess
import os
from tempfile import NamedTemporaryFile
from datetime import datetime
import zipfile

from flask import (Blueprint, redirect, render_template, flash, views,
                   url_for, g, send_file, current_app, request, abort)
from flask.ext import login as flask_login

from sanap.auth import login_required, eea_admin
from sanap.models import Survey
from sanap.forms import SurveyForm
from sanap.forms.survey import FILE_FIELDS, files
from sanap import assets as sanap_assets
from sanap import emails


survey = Blueprint('survey', __name__)


def initialize_app(app):
    app.register_blueprint(survey)


def export_pdf(survey):
    """Generate pdf file out of a Survey object. File handler left open"""
    proj_dir = os.path.dirname(__file__)
    source = Edit().get(survey.id)
    inject_css = ''
    for css in sanap_assets.BUNDLE_CSS + sanap_assets.BUNDLE_PRINT_CSS:
        css_file = open(os.path.join(proj_dir, "static", css), "r")
        inject_css += css_file.read()
        css_file.close()
    source = source.replace("<head>",
                         "<head><style type='text/css'>%s</style>" % inject_css)
    html_infile = NamedTemporaryFile(suffix='.html')
    html_infile.write(source.encode("utf-8"))
    html_infile.flush()

    pdf_outfile = NamedTemporaryFile(suffix='.pdf')

    retcode = subprocess.call(['wkhtmltopdf', '-O', 'Landscape', '-q',
                                html_infile.name, pdf_outfile.name])
    html_infile.close()
    return pdf_outfile


class Home(views.MethodView):

    decorators = (login_required,)

    def get(self):
        surveys = Survey.objects.filter(country=g.user.country) \
                                .order_by('for_eea')
        return render_template('index.html', surveys=surveys)

survey.add_url_rule('/', view_func=Home.as_view('home'))


class Edit(views.MethodView):

    decorators = (login_required,)

    def get(self, survey_id=None):

        survey = None

        if survey_id:
            survey = Survey.objects.get_or_404(id=survey_id)
        else:
            crt_user = flask_login.current_user
            if crt_user.is_coordinator:
                # see if coordinated country has one
                survey = Survey.objects.filter(country=crt_user.country,
                                               for_eea=True).first()
            else:
                # see if user already has one
                survey = Survey.objects.filter(user=crt_user.id).first()

        if not survey_id and survey:
            return redirect(url_for('.edit', survey_id=survey.id))
        elif survey:
            form = SurveyForm(obj=survey)
        else:
            form = SurveyForm()

        return render_template('edit.html', form=form, survey_id=survey_id)

    def post(self, survey_id=None):
        if survey_id:
            survey = Survey.objects.get_or_404(id=survey_id)
            form = SurveyForm(obj=survey)
            if not survey.draft:
                flash(('Your changes were not saved. This self-assessment'
                       ' has been previously submitted and closed.'), 'error')
                return render_template('edit.html', form=form)
        else:
            survey = None
            form = SurveyForm()
        if form.validate():
            obj = form.save(survey=survey)
            pdf = request.form.get('export_pdf', '')
            if obj.draft:
                flash_msg = 'Your self-assessment has been saved as a draft. '
                if obj.for_eea:
                    flash_msg += ('When it is final, don\'t forget to submit the'
                                  ' final version to the EEA.')
                else:
                    flash_msg += ('When it is final, don\'t forget to submit the'
                                  ' final version to your country coordinator.')
            else:
                obj.user = flask_login.current_user._get_current_object()
                obj.save()
                if obj.for_eea:
                    flash_msg = 'The final version of the self-assessment (%s) has been submitted.' % obj.country
                    emails.country_submitted(obj)
                else:
                    flash_msg = 'Your self-assessment has been submitted.'
                    emails.contact_submitted(obj)
            if pdf:
                flash_msg += ("""<br /><br />The <img src="../static/img/pdf.png" /> PDF
                              of your latest version of the self-assessment is ready;
                                you can <a href="%s" target="_blank">click here to download it</a>.
                                <br />You can also <a href="%s">download a ZIP bundle</a>,
                                including any uploaded files in this self-assessment.
                              """ % (url_for("survey.export", survey_id=obj.id),
                                     url_for("survey.report", survey_id=obj.id)))
            flash(flash_msg)
            return redirect(url_for('.edit', survey_id=obj.id))

        return render_template('edit.html', form=form)

survey.add_url_rule('/add', view_func=Edit.as_view('edit'))
survey.add_url_rule('/edit/<string:survey_id>', view_func=Edit.as_view('edit'))


@survey.route("/glossary")
def glossary():
    return render_template('glossary.html')


@survey.route("/export/<string:survey_id>")
@login_required
def export(survey_id):
    survey = Survey.objects.get_or_404(id=survey_id)
    filename = 'sanap-%s-%s.pdf' % (survey.country,
                                datetime.now().strftime("%Y-%m-%d %H.%M"))

    pdf_file = export_pdf(survey)
    response = send_file(pdf_file.name, mimetype='application/pdf')
    response.headers['Content-Disposition'] = ('attachment; filename="%s"'
                                               % filename)

    pdf_file.close()
    return response


@survey.route("/report/<string:survey_id>")
@login_required
def report(survey_id):
    survey = Survey.objects.get_or_404(id=survey_id)
    filename = 'sanap-%s-%s.pdf' % (survey.country,
                                datetime.now().strftime("%Y-%m-%d %H.%M"))

    pdf_file = export_pdf(survey)
    zip_file = NamedTemporaryFile(suffix='.zip')
    tmp_name = zip_file.name
    zip_obj = zipfile.ZipFile(zip_file, "w")
    zip_obj.write(pdf_file.name, filename)
    for filefield in FILE_FIELDS:
        for fileinstance in getattr(survey, filefield):
            abspath = files.path(fileinstance)
            arcname = "uploads/%s" % abspath.rsplit(os.sep, 1)[-1]
            zip_obj.write(abspath, arcname)
    zip_obj.close()
    pdf_file.close()
    response = send_file(tmp_name, mimetype='application/zip')
    response.headers['Content-Disposition'] = (('attachment; '
                                                'filename="%s-full-report.zip"')
                                               % survey.country)
    return response


class Contacts(views.MethodView):

    decorators = (login_required, )

    def get(self):
        if not g.user.token:
            abort(403)

        form = SurveyForm()
        surveys = Survey.objects.filter(country=g.user.country, for_eea=False,
                                        draft=False)
        return render_template('contacts.html', form=form, surveys=surveys)

survey.add_url_rule('/contacts', view_func=Contacts.as_view('contacts'))


class Dashboard(views.MethodView):

    decorators = (login_required, eea_admin)

    def get(self):
        form = SurveyForm()
        surveys = Survey.objects.filter(for_eea=True, draft=False)
        return render_template('dashboard.html', form=form, surveys=surveys)

survey.add_url_rule('/dashboard', view_func=Dashboard.as_view('dashboard'))


