from flask import g
from flask.ext import wtf
from flask.ext.mongoengine.wtf import model_form
from flask.ext.uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES

from sanap.models import Survey
from sanap.forms.fields import *
from sanap.model_data import *


files = UploadSet('files', AllExcept(SCRIPTS + EXECUTABLES))
_SurveyForm = model_form(Survey)
FILE_FIELDS = ('assessment_subnational_files', 'action_plan_files',
               'part4_files', 'part2_files', 'part1_files', 'part3_files',)


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

    lead_organisation = wtf.TextField(Q['lead_organisation'])

    organisations = Tagit(Q['organisations'])

    country = wtf.TextField()

    public_awareness = CustomRadioField(Q['1'], choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    adaptation_need = CustomRadioField(Q['2'], choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    triggers = MultiCheckboxField(Q['3'], choices=TRIGGERS,
        validators=[wtf.validators.optional()])

    willingness = CustomRadioField(Q['4'], choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    knowledge = CustomRadioField(Q['5'], choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    uncertainties = CustomRadioField(Q['6'], choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    objectives = CustomRadioField(Q['7'], choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    integration = CustomRadioField(Q['8'], choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    integration_examples = wtf.TextAreaField(Q['provide_examples'])

    mitigation = CustomRadioField(Q['9'], choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    mitigation_examples = wtf.TextAreaField(Q['provide_examples'])

    transnational_cooperation = CustomRadioField(Q['10'], choices=AGREEMENT,
        validators=[wtf.validators.optional()])

    transnational_cooperation_examples = wtf.TextAreaField(Q['provide_examples'])

    barriers = MultiCheckboxField(Q['11'], choices=BARRIERS,
        validators=[wtf.validators.optional()])

    part1_comments = wtf.TextAreaField(Q['p1comments'])

    part1_files =  CustomFileField(Q['files'],
       validators=[wtf.file_allowed(files, 'Document is not valid')])

    ## part2

    process_stage = CustomRadioField(Q['12'], choices=PROCESS_STAGE,
        validators=[wtf.validators.optional()])

    horizontal_integration = CustomRadioField(Q['13'], choices=EFFECTIVENESS,
        validators=[wtf.validators.optional()])

    vertical_integration = CustomRadioField(Q['14'], choices=EFFECTIVENESS,
        validators=[wtf.validators.optional()])

    horizontal_coordination = wtf.TextAreaField(Q['h_coordination'])

    vertical_coordination = wtf.TextAreaField(Q['v_coordination'])

    crucial_in_coordination = wtf.TextAreaField(Q['c_coordination'])

    challenging_in_coordination = wtf.TextAreaField(Q['m_coordination'])

    assessment = CustomRadioField(Q['16'], choices=STATUS,
        validators=[wtf.validators.optional()])

    assessment_scale = MultiCheckboxField(Q['if_yes'], choices=ASSESSMENT_SCALE,
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
            if key in ('organisations',
                       'country', 'for_eea', 'user', 'draft') + FILE_FIELDS:
                continue
            if value:
                setattr(survey, key, value)

        organisations = self.data['organisations'].split(',')
        if organisations:
            survey.organisations = organisations

        for field_name in FILE_FIELDS:
            uploaded = self.data[field_name]
            if uploaded:
                value = getattr(survey, field_name, False) or []
                value.append(files.save(uploaded))
                setattr(survey, field_name, value)

        survey.save()
        return survey
