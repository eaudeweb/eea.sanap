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

    country = db.StringField(max_length=128, choices=COUNTRIES)

    roles = db.ListField(db.StringField(), default=[])

    invite = db.ReferenceField('Invite', default=None)

    def get_id(self):
        return self.id

    @property
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Survey(db.Document):

    country = db.StringField(max_length=128, choices=COUNTRIES)

    user = db.ReferenceField(User)

    for_eea = db.BooleanField(default=True)

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
    horizontal_integration = db.StringField(choices=EFFECTIVENESS)

    vertical_integration = db.StringField(choices=EFFECTIVENESS)

    horizontal_coordination = db.StringField(max_length=512)

    vertical_coordination = db.StringField(max_length=512)

    crucial_in_coordination = db.StringField(max_length=512)

    challenging_in_coordination = db.StringField(max_length=512)

    assessment = db.StringField(choices=STATUS)

    #TODO sectors_assessments

    assessment_coordination = db.StringField(max_length=512)

    assessment_methodological_approach = db.StringField(max_length=512)

    needed_info = db.ListField(db.StringField(), default=[])

    assessment_update = db.StringField(choices=PLANNING)

    adaptation_options = db.StringField(choices=STATUS)

    adaptation_scale = db.ListField(db.StringField(), default=[])

    identified_options = db.ListField(db.StringField(), default=[])

    options_comments = db.StringField(max_length=512)

    adaptation_actions = db.ListField(db.StringField(), default=[])

    practice_example = db.StringField(max_length=512)

    integrating_plans = db.StringField(max_length=512)

    monitor_report_evaluate = db.DictField(default={})

    part2_comments = db.StringField(max_length=512)

    # part 3
    # TODOsectors

    main_instruments = db.DictField(default={})

    main_instruments_considered = db.StringField(max_length=512)


class Invite(db.Document):

    key = db.StringField(max_length=36)

    country = db.StringField(choices=COUNTRIES)

    invitee = db.ReferenceField(User)

    assessment_scale = db.ListField(db.StringField(), default=[])
