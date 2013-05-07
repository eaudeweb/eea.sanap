from flask import (Blueprint, redirect, render_template, flash, views,
                   url_for, g, send_file, current_app, request, abort)
from flask.ext import login as flask_login

from sanap.auth import login_required
from sanap.models import Survey
from sanap.forms import SurveyForm
from sanap import assets as sanap_assets


survey = Blueprint('survey', __name__)


def initialize_app(app):
    app.register_blueprint(survey)


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

        return render_template('edit.html', form=form)

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
            if obj.draft:
                flash('Your self-assessment has been saved.')
            else:
                flash('Your self-assessment has been submitted.')
            # hackish, but users might export the form before saving it
            if request.form.get('export_pdf'):
                return export(survey_id)
            return redirect(url_for('.edit', survey_id=obj.id))

        return render_template('edit.html', form=form)

survey.add_url_rule('/add', view_func=Edit.as_view('edit'))
survey.add_url_rule('/edit/<string:survey_id>', view_func=Edit.as_view('edit'))


@survey.route("/download_docx")
def download_docx():
    import os
    fname = "Adaptation Policy Process Self-Assessment 2013.docx"
    survey_file = os.path.join(os.path.dirname(__file__), "static", fname)
    response = send_file(survey_file, mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response.headers[u"Content-Disposition"] = ('attachment; filename="%s"' %
                                                fname)
    return response


@survey.route("/download_glossary/<string:fmt>")
def download_glossary(fmt):
    mimetypes = {'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                 'pdf': 'application/pdf'}
    assert fmt in mimetypes, "Incorrect file format"
    import os
    fname = "Self-Assessment Glossary.%s" % fmt
    glossary_file = os.path.join(os.path.dirname(__file__), "static", fname)

    response = send_file(glossary_file, mimetype=mimetypes[fmt])
    response.headers[u"Content-Disposition"] = ('attachment; filename="%s"' %
                                                fname)
    return response


@survey.route("/glossary")
def glossary():
    return render_template('glossary.html')


@survey.route("/export/<string:survey_id>")
@login_required
def export(survey_id):
    import subprocess
    import os
    from tempfile import NamedTemporaryFile
    from datetime import datetime

    proj_dir = os.path.dirname(__file__)
    source = Edit().get(survey_id)
    survey = Survey.objects.get_or_404(id=survey_id)
    filename = 'sanap-%s-%s' % (survey.country,
                                datetime.now().strftime("%Y-%m-%d %H:%M"))

    inject_css = ''
    for css in sanap_assets.BUNDLE_CSS:
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
    response = send_file(pdf_outfile.name, mimetype='application/pdf')
    response.headers['Content-Disposition'] = ('attachment; filename=' +
                                       filename + '.pdf')

    pdf_outfile.close()
    html_infile.close()

    return response


@survey.route("/contacts")
@login_required
def contacts():
    if not g.user.token:
        abort(403)
    return render_template('contacts.html')
