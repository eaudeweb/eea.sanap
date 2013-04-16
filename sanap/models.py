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

    roles = db.ListField(db.StringField(), default=[])

    def get_id(self):
        return self.id

    @property
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)
