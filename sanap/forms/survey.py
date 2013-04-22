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

    action_plan_file =  CustomFileField(
       validators=[wtf.file_allowed(files, 'Document is not valid')])

    monitor_report_evaluate = wtf.FormField(MonitorReportEvaluateForm,
        widget=MatrixCheckboxWidget(data=MONITOR_REPORT_EVALUATE))

    instruments = wtf.RadioField(choices=INSTRUMENTS,
        validators=[wtf.validators.optional()])

    main_instruments = wtf.FormField(MainInstrumentsForm,
        widget=MatrixCheckboxWidget(data=MAIN_INSTRUMENTS, id='main-instruments'))


    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        expand_choices(self.triggers)

    def save(self):
        survey = Survey()

        survey.lead_organisation = self.data['lead_organisation']

        organisations = self.data['organisations'].split(',')
        if organisations:
            survey.organisations = organisations

        survey.public_awareness = self.data['public_awareness']
        survey.adaptation_need = self.data['adaptation_need']
        survey.willingness = self.data['willingness']
        survey.triggers = self.data['triggers']
        survey.knowledge = self.data['knowledge']
        survey.uncertainties = self.data['uncertainties']
        survey.objectives = self.data['objectives']
        survey.integration = self.data['integration']
        survey.integration_examples = self.data['integration_examples']
        survey.mitigation = self.data['mitigation']
        survey.mitigation_examples = self.data['mitigation_examples']
        survey.transnational_cooperation = self.data['transnational_cooperation']
        survey.transnational_cooperation_examples = self.data['transnational_cooperation_examples']
        survey.barriers = self.data['barriers']
        survey.part1_comments = self.data['part1_comments']
        survey.process_stage = self.data['process_stage']
        survey.horizontal_integration = self.data['horizontal_integration']
        survey.vertical_integration = self.data['vertical_integration']
        survey.horizontal_coordination = self.data['horizontal_coordination']
        survey.vertical_coordination = self.data['vertical_coordination']
        survey.crucial_in_coordination = self.data['crucial_in_coordination']
        survey.challenging_in_coordination = self.data['challenging_in_coordination']
        survey.assessment = self.data['assessment']
        survey.assessment_coordination = self.data['assessment_coordination']
        survey.assessment_methodological_approach = self.data['assessment_methodological_approach']
        survey.change_adaptation_costs = self.data['change_adaptation_costs']
        survey.needed_info = self.data['needed_info']
        survey.assessment_update = self.data['assessment_update']
        survey.assessment_update_info = self.data['assessment_update_info']
        survey.adaptation_options = self.data['adaptation_options']
        survey.adaptation_scale = self.data['adaptation_scale']
        survey.assessment_subnational_info = self.data['assessment_subnational_info']
        #TODO assessment_subnational_files
        survey.identified_options = self.data['identified_options']

        survey.adaptation_actions = self.data['adaptation_actions']
        survey.prioritised_options = self.data['prioritised_options']
        survey.options_methodological = self.data['options_methodological']
        survey.action_plan_info = self.data['action_plan_info']
        #TODO action_plan_file
        survey.practice_example = self.data['practice_example']
        survey.monitor_report_evaluate = self.data['monitor_report_evaluate']
        survey.part2_comments = self.data['part2_comments']
        survey.instruments = self.data['instruments']

        return survey
