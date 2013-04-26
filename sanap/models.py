import re
from unicodedata import normalize

from flask.ext.mongoengine import MongoEngine
from flask.ext.login import UserMixin
from werkzeug.utils import cached_property

from sanap.model_data import *


db = MongoEngine()


class User(db.Document, UserMixin):

    id = db.StringField(max_length=64, required=True, primary_key=True)

    first_name = db.StringField(max_length=128, required=True)

    last_name = db.StringField(max_length=128, required=True)

    email = db.StringField(max_length=128, required=True)

    phone_number = db.StringField(max_length=32)

    organisation = db.StringField(max_length=128)

    country = db.StringField(choices=COUNTRIES)

    last_login = db.DateTimeField()

    invitee = db.ReferenceField('User', default=None)

    token = db.StringField(max_length=36, default=None)

    def __unicode__(self):
        return self.name

    def get_id(self):
        return self.id

    @property
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Survey(db.Document):

    meta = {
        'ordering': ('-for_eea',)
    }

    country = db.StringField(max_length=128, choices=COUNTRIES)

    user = db.ReferenceField(User)

    for_eea = db.BooleanField(default=True)

    draft = db.BooleanField(default=True)

    lead_organisation = db.StringField(max_length=512)

    organisations = db.ListField(db.StringField(), default=[])

    public_awareness = db.StringField()

    adaptation_need = db.StringField(choices=AGREEMENT)

    willingness = db.StringField(choices=AGREEMENT)

    triggers = db.ListField(db.StringField(max_length=512), default=[])

    knowledge = db.StringField(choices=AGREEMENT)

    uncertainties = db.StringField(choices=AGREEMENT)

    objectives = db.StringField(choices=AGREEMENT)

    integration = db.StringField(choices=AGREEMENT)

    integration_examples = db.StringField(max_length=2056)

    mitigation = db.StringField(choices=AGREEMENT)

    mitigation_examples = db.StringField(max_length=2056)

    transnational_cooperation = db.StringField(choices=AGREEMENT)

    transnational_cooperation_examples = db.StringField(max_length=2056)

    barriers = db.ListField(db.StringField(), default=[])

    part1_comments = db.StringField(max_length=2056)

    # part 2

    process_stage = db.StringField(choices=PROCESS_STAGE)

    horizontal_integration = db.StringField(choices=EFFECTIVENESS)

    vertical_integration = db.StringField(choices=EFFECTIVENESS)

    horizontal_coordination = db.StringField(max_length=512)

    vertical_coordination = db.StringField(max_length=512)

    crucial_in_coordination = db.StringField(max_length=512)

    challenging_in_coordination = db.StringField(max_length=512)

    assessment = db.StringField(choices=STATUS)

    assessment_scale = db.StringField(choices=ASSESSMENT_SCALE)

    assessment_subnational_info = db.StringField(max_length=512)

    assessment_subnational_files = db.StringField(max_length=512)

    #TODO sectors_assessments

    assessment_coordination = db.StringField(max_length=512)

    assessment_methodological_approach = db.StringField(max_length=512)

    change_adaptation_costs = db.StringField(max_length=512)

    needed_info = db.ListField(db.StringField(), default=[])

    assessment_update = db.StringField(choices=PLANNING)

    assessment_update_info = db.StringField(max_length=512)

    adaptation_options = db.StringField(choices=STATUS)

    adaptation_scale = db.ListField(db.StringField(), default=[])

    identified_options = db.ListField(db.StringField(), default=[])

    adaptation_actions = db.ListField(db.StringField(), default=[])

    prioritised_options = db.StringField(choices=STATUS)

    options_methodological = db.StringField(max_length=512)

    action_plan_info = db.StringField(max_length=512)

    action_plan_files = db.StringField(max_length=512)

    practice_example = db.StringField(max_length=512)

    integrating_plans = db.StringField(max_length=512)

    monitor_report_evaluate = db.DictField(default={})

    part2_comments = db.StringField(max_length=512)

    part2_files = db.StringField(max_length=512)

    # part 3
    # TODOsectors

    instruments = db.StringField(choices=INSTRUMENTS)

    main_instruments = db.DictField(default={})

    main_instruments_considered = db.StringField(max_length=512)

    financing_mechanisms = db.DictField(default={})

    part3_comments = db.StringField(max_length=512)

    part3_files = db.StringField(max_length=512)

    transboundary_issues = db.StringField(max_length=512)

    regions_coordination = db.StringField(max_length=512)

    # part 4

    stakeholders_involved = db.StringField(choices=YES_NO)

    stakeholders_contribution = db.StringField(choices=STAKEHOLDERS_CONTRIBUTION)

    development_involvement = db.DictField(default={})

    implementation_involvement = db.DictField(default={})

    monitoring_involvement = db.DictField(default={})

    stakeholders_success = db.StringField(max_length=512)

    part4_comments = db.StringField(max_length=512)

    part4_files = db.StringField(max_length=512)

    # part 5
    next_step_vulnerability = db.StringField(max_length=512)

    next_step_legislation = db.StringField(max_length=512)

    next_step_implementation = db.StringField(max_length=512)

    next_step_monitoring = db.StringField(max_length=512)

    next_step_strategy = db.StringField(max_length=512)

    next_step_others = db.StringField(max_length=512)

    adaptation_key_issues = db.StringField(max_length=512)

    adaptation_support_eu_level = db.StringField(max_length=512)

    def __unicode__(self):
        return self.country


_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))
