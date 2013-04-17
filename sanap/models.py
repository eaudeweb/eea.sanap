from flask.ext.mongoengine import MongoEngine
from flask.ext.login import UserMixin
from werkzeug.utils import cached_property

from sanap.model_data import *


db = MongoEngine()


class User(db.Document, UserMixin):

    id = db.StringField(max_length=16, required=True, primary_key=True)

    first_name = db.StringField(max_length=128, required=True)

    last_name = db.StringField(max_length=128, required=True)

    email = db.StringField(max_length=128, required=True)

    phone_number = db.StringField(max_length=32)

    organisation = db.StringField(max_length=128)

    last_login = db.DateTimeField()

    country = db.StringField(max_length=128, choices=COUNTRIES)

    roles = db.ListField(db.StringField(), default=[])

    def get_id(self):
        return self.id

    @property
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Survey(db.Document):

    country = db.StringField(max_length=128, choices=COUNTRIES)

    lead_organisation = db.StringField(max_length=256)

    organisations = db.ListField(db.StringField(), default=[])

    public_awareness = db.StringField(choices=AGREEMENT)

    adaptation_need = db.StringField(choices=AGREEMENT)

    willingness = db.StringField(choices=AGREEMENT)

    triggers = db.ListField(db.StringField(max_length=256), default=[])

    knowledge = db.StringField(choices=AGREEMENT)

    uncertainties = db.StringField(choices=AGREEMENT)

    goals = db.StringField(choices=AGREEMENT)

    integration = db.StringField(choices=AGREEMENT)

    integration_examples = db.StringField(max_length=2056)

    mitigation = db.StringField(choices=AGREEMENT)

    mitigation_examples = db.StringField(max_length=2056)

    transnational_cooperation = db.StringField(choices=AGREEMENT)

    transnational_cooperation_examples = db.StringField(max_length=2056)

    monitoring = db.StringField(choices=AGREEMENT)

    barriers = db.ListField(db.StringField(max_length=256), default=[])

    part1_comments = db.StringField(max_length=2056)

