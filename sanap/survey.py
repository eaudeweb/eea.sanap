from flask import (Blueprint, redirect, render_template, flash, views,
                   url_for, g)
from sanap.auth import login_required
from sanap.models import Survey
from sanap.forms import SurveyForm


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
        if survey_id:
            survey = Survey.objects.get_or_404(id=survey_id)
            form = SurveyForm(obj=survey)
        else:
            form = SurveyForm()
        return render_template('edit.html', form=form)

    def post(self, survey_id=None):
        if survey_id:
            survey = Survey.objects.get_or_404(id=survey_id)
            form = SurveyForm(obj=survey)
        else:
            survey = None
            form = SurveyForm()
        if form.validate():
            obj = form.save(survey=survey)
            flash('Survey added successfully')
            return redirect(url_for('.edit', survey_id=obj.id))
        return render_template('edit.html', form=form)

survey.add_url_rule('/add', view_func=Edit.as_view('edit'))
survey.add_url_rule('/edit/<string:survey_id>', view_func=Edit.as_view('edit'))


