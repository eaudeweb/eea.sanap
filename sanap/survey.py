from flask import (Blueprint, redirect, render_template, flash, views, url_for)
from flask.ext.login import login_required
from sanap.models import Survey
from sanap.forms import SurveyForm


survey = Blueprint('survey', __name__)


def initialize_app(app):
    app.register_blueprint(survey)


class Home(views.MethodView):

    def get(self):
        return redirect(url_for('.add'))

survey.add_url_rule('/',
    view_func=login_required(Home.as_view('home')))


class Edit(views.MethodView):

    def get(self):
        form = SurveyForm()
        return render_template('edit.html', form=form)

    def post(self):
        form = SurveyForm()
        if form.validate():
            form.save()
            flash('Survey added successfully')
        return render_template('edit.html', form=form)

survey.add_url_rule('/add',
    view_func=login_required(Edit.as_view('edit')))
