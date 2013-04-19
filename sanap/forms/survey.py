from flask.ext import wtf
from flask.ext.mongoengine.wtf import model_form

from sanap.models import Survey
from sanap.forms.fields import MultiCheckboxField, expand_choices
from sanap.model_data import *


_SurveyForm = model_form(Survey)


class SurveyForm(_SurveyForm):

    organisations = wtf.TextField()

    public_awareness = wtf.RadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    adaptation_need = wtf.RadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    triggers = MultiCheckboxField(choices=TRIGGERS,
        validators=[wtf.validators.optional()])

    knowledge = wtf.RadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    uncertainties = wtf.RadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    goals = wtf.RadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    integration = wtf.RadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    monitoring = wtf.RadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    barriers = MultiCheckboxField(choices=BARRIERS,
        validators=[wtf.validators.optional()])

    horizontal_integration = wtf.RadioField(choices=EFFECTIVENESS,
        validators=[wtf.validators.optional()])

    vertical_integration = wtf.RadioField(choices=EFFECTIVENESS,
        validators=[wtf.validators.optional()])

    assessment = wtf.RadioField(choices=STATUS,
        validators=[wtf.validators.optional()])

    needed_info = MultiCheckboxField(choices=BARRIERS,
        validators=[wtf.validators.optional()])

    assessment_update = wtf.RadioField(choices=PLANNING,
        validators=[wtf.validators.optional()])

    adaptation_options = wtf.RadioField(choices=STATUS,
        validators=[wtf.validators.optional()])

    adaptation_scale = MultiCheckboxField(choices=ADAPTATION_SCALE,
        validators=[wtf.validators.optional()])

    identified_options = MultiCheckboxField(choices=IDENTIFIED_OPTIONS,
        validators=[wtf.validators.optional()])

    adaptation_actions = MultiCheckboxField(choices=ADAPTATION_ACTIONS,
        validators=[wtf.validators.optional()])

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        expand_choices(self.triggers)

    def save(self):
        survey = Survey()

        survey.lead_organisation = self.data['lead_organisation']

        organisations = self.data['organisations'].split(',')
        if organisations:
            survey.organisations = organisations

        adaptation_need = self.data['adaptation_need'].split(',')
        if organisations:
            survey.adaptation_need = adaptation_need

        willingness = self.data['adaptation_need'].split(',')
        if willingness:
            survey.willingness = adaptation_need

        return survey
