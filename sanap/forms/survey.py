from flask import g
from flask.ext import wtf
from flask.ext.mongoengine.wtf import model_form
from flask.ext.uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES

from sanap.models import Survey
from sanap.forms.fields import *
from sanap.model_data import *


files = UploadSet('files', AllExcept(SCRIPTS + EXECUTABLES))
_SurveyForm = model_form(Survey)


class SectorsForm(wtf.Form):

    adaptation_national = MultiTextField()

    adaptation_sub_national = MultiTextField()

    adaptation_local = MultiTextField()

    priority_sectors = MultiCheckboxField()

    examples = MultiTextField()


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


class InvolmentForm(wtf.Form):

    information_given =  MultiCheckboxField()

    information_gathered = MultiCheckboxField()

    consultation = MultiCheckboxField()

    active_involvement = MultiCheckboxField()

    partnerships = MultiCheckboxField()

    empowerment = MultiCheckboxField()


class SurveyForm(_SurveyForm):

    draft = CustomBoolean()

    organisations = Tagit()

    country = wtf.TextField()

    public_awareness = CustomRadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    adaptation_need = CustomRadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    triggers = MultiCheckboxField(choices=TRIGGERS,
        validators=[wtf.validators.optional()])

    willingness = CustomRadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    knowledge = CustomRadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    uncertainties = CustomRadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    objectives = CustomRadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    goals = CustomRadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    integration = CustomRadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    integration_examples = wtf.TextAreaField()

    mitigation = CustomRadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    mitigation_examples = wtf.TextAreaField()

    transnational_cooperation = CustomRadioField(choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    transnational_cooperation_examples = wtf.TextAreaField()

    barriers = MultiCheckboxField(choices=BARRIERS,
        validators=[wtf.validators.optional()])

    part1_comments = wtf.TextAreaField()

    process_stage = CustomRadioField(choices=PROCESS_STAGE,
        validators=[wtf.validators.optional()])

    horizontal_integration = CustomRadioField(choices=EFFECTIVENESS,
        validators=[wtf.validators.optional()])

    vertical_integration = CustomRadioField(choices=EFFECTIVENESS,
        validators=[wtf.validators.optional()])

    assessment = CustomRadioField(choices=STATUS,
        validators=[wtf.validators.optional()])

    assessment_scale = CustomRadioField(choices=ASSESSMENT_SCALE,
        validators=[wtf.validators.optional()])

    assessment_subnational_files = CustomFileField(
       validators=[wtf.file_allowed(files, 'Document is not valid')])

    needed_info = MultiCheckboxField(choices=BARRIERS,
        validators=[wtf.validators.optional()])

    assessment_update = CustomRadioField(choices=PLANNING,
        validators=[wtf.validators.optional()])

    adaptation_options = CustomRadioField(choices=STATUS,
        validators=[wtf.validators.optional()])

    adaptation_scale = MultiCheckboxField(choices=ADAPTATION_SCALE,
        validators=[wtf.validators.optional()])

    identified_options = MultiCheckboxField(choices=IDENTIFIED_OPTIONS,
        validators=[wtf.validators.optional()])

    adaptation_actions = MultiCheckboxField(choices=ADAPTATION_ACTIONS,
        validators=[wtf.validators.optional()])

    prioritised_options = CustomRadioField(choices=STATUS,
        validators=[wtf.validators.optional()])

    action_plan_files = CustomFileField(
       validators=[wtf.file_allowed(files, 'Document is not valid')])

    monitor_report_evaluate = wtf.FormField(MonitorReportEvaluateForm,
        widget=MatrixCheckboxWidget(data=MONITOR_REPORT_EVALUATE))

    sectors = wtf.FormField(SectorsForm, widget=MatrixCheckboxWidget(
        data=SECTORS, id='sectors'))

    instruments = CustomRadioField(choices=INSTRUMENTS,
        validators=[wtf.validators.optional()])

    main_instruments = wtf.FormField(MainInstrumentsForm,
        widget=MatrixCheckboxWidget(data=MAIN_INSTRUMENTS, id='main-instruments'))

    part2_files =  CustomFileField(
       validators=[wtf.file_allowed(files, 'Document is not valid')])

    financing_mechanisms = wtf.FormField(MainInstrumentsForm,
        widget=MatrixCheckboxWidget(data=FINANCING_MECHANISMS))

    part3_files = CustomFileField(
       validators=[wtf.file_allowed(files, 'Document is not valid')])

    stakeholders_involved = CustomRadioField(choices=YES_NO,
        validators=[wtf.validators.optional()])

    stakeholders_contribution = CustomRadioField(choices=STAKEHOLDERS_CONTRIBUTION,
        validators=[wtf.validators.optional()])

    development_involvement = wtf.FormField(InvolmentForm,
        widget=MatrixCheckboxWidget(data=INVOLMENT))

    implementation_involvement = wtf.FormField(InvolmentForm,
        widget=MatrixCheckboxWidget(data=INVOLMENT))

    monitoring_involvement = wtf.FormField(InvolmentForm,
        widget=MatrixCheckboxWidget(data=INVOLMENT))

    part4_files = CustomFileField(
       validators=[wtf.file_allowed(files, 'Document is not valid')])

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        expand_choices(self.triggers)

    def save(self, survey):
        user = g.user._get_current_object()

        survey = survey or Survey()
        survey.user = user
        survey.country = user.country
        survey.for_eea = False if user.invitee else True
        survey.draft = True if self.data['draft'] else False

        for key, value in self.data.items():
            if key in ('organisations', 'assessment_subnational_files',
                       'action_plan_files', 'country',
                       'for_eea', 'user', 'draft'):
                continue
            if value:
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

        part4_files = self.data['part4_files']
        if part4_files:
            survey.part4_files = files.save(part4_files)

        survey.save()
        return survey
