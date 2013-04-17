from flask import (Blueprint, render_template)
from sanap.models import Survey


survey = Blueprint('survey', __name__)


def initialize_app(app):
    app.register_blueprint(survey)


@survey.route('/add', methods=['GET', 'POST'])
def edit():
    return render_template('edit.html')