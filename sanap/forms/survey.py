from flask.ext import wtf
from flask.ext.mongoengine.wtf import model_form
from flask.ext.uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES

from sanap.models import Survey
from sanap.forms.fields import *
from sanap.model_data import *


files = UploadSet('files', AllExcept(SCRIPTS + EXECUTABLES))
_SurveyForm = model_form(Survey)


class MonitorReportEvaluateForm(wtf.Form):

    not_planed_yet = MultiCheckboxField()

    under_development = MultiCheckboxField()

    implemented = MultiCheckboxField()


class MainInstrumentsForm(wtf.Form):

    agriculture = MultiCheckboxField()

    forestry = MultiCheckboxField()

    biodiversity = MultiCheckboxField()

    human_health = MultiCheckboxField()

    water = MultiCheckboxField()

    marine_fisheries = MultiCheckboxField()

    coastal_areas = MultiCheckboxField()

    mountain_areas = MultiCheckboxField()

    tourism = MultiCheckboxField()

    transport = MultiCheckboxField()

    energy = MultiCheckboxField()

    built_environment = MultiCheckboxField()

    spatial_planning = MultiCheckboxField()

    civil_protection = MultiCheckboxField()

    industry = MultiCheckboxField()

    business_services = MultiCheckboxField()

    financial_insurance = MultiCheckboxField()

    cultural_heritage = MultiCheckboxField()


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

    barriers = MultiCheckboxField(choices=BARRIERS,
        validators=[wtf.validators.optional()])

    process_stage = wtf.RadioField(choices=PROCESS_STAGE,
        validators=[wtf.validators.optional()])

    horizontal_integration = wtf.RadioField(choices=EFFECTIVENESS,
        validators=[wtf.validators.optional()])

    vertical_integration = wtf.RadioField(choices=EFFECTIVENESS,
        validators=[wtf.validators.optional()])

    assessment = wtf.RadioField(choices=STATUS,
        validators=[wtf.validators.optional()])

    assessment_scale = wtf.RadioField(choices=ASSESSMENT_SCALE,
        validators=[wtf.validators.optional()])

    assessment_subnational_files = CustomFileField(
       validators=[wtf.file_allowed(files, 'Document is not valid')])

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

    prioritised_options = wtf.RadioField(choices=STATUS,
        validators=[wtf.validators.optional()])

    action_plan_files = CustomFileField(
       validators=[wtf.file_allowed(files, 'Document is not valid')])

    monitor_report_evaluate = wtf.FormField(MonitorReportEvaluateForm,
        widget=MatrixCheckboxWidget(data=MONITOR_REPORT_EVALUATE))

    instruments = wtf.RadioField(choices=INSTRUMENTS,
        validators=[wtf.validators.optional()])

    main_instruments = wtf.FormField(MainInstrumentsForm,
        widget=MatrixCheckboxWidget(data=MAIN_INSTRUMENTS, id='main-instruments'))

    part2_files =  CustomFileField(
       validators=[wtf.file_allowed(files, 'Document is not valid')])

    financing_mechanisms = wtf.FormField(MainInstrumentsForm,
        widget=MatrixCheckboxWidget(data=FINANCING_MECHANISMS))

    part3_files =  CustomFileField(
       validators=[wtf.file_allowed(files, 'Document is not valid')])

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        expand_choices(self.triggers)

    def save(self):
        survey = Survey()

        for key, value in self.data.items():
            if key in ('organisations', 'assessment_subnational_files',
                       'action_plan_files'):
                continue
            setattr(survey, key, value)

        organisations = self.data['organisations'].split(',')
        if organisations:
            survey.organisations = organisations

        assessment_subnational_files = self.data['assessment_subnational_files']
        if assessment_subnational_files:
            survey.assessment_subnational_files = files.save(assessment_subnational_files)

        action_plan_files = self.data['action_plan_files']
        if action_plan_files:
            survey.action_plan_files = files.save(action_plan_files)

        return survey
