import re

from flask.ext.login import current_user
from flask_mail import Message, Mail
from flask import render_template, current_app

from sanap.models import User

mail = Mail()


def striptags(value):

    return re.sub(r'(<!--.*?-->|<[^>]*>)', '', value)


def country_submitted(survey):

    coordinators = User.objects.filter(country=survey.country, invitee=None)
    msg = Message("Final Version of Self-Assessment Submitted to the EEA",
                  recipients=[user.email for user in coordinators])
    html = render_template("emails/country_submitted.html", survey=survey,
                           user=current_user)
    msg.html = html
    msg.body = striptags(html)
    mail.send(msg)


def contact_submitted(survey):

    coordinators = User.objects.filter(country=survey.country, invitee=None)
    msg = Message("Self-Assessment submitted by country contact",
                  recipients=[user.email for user in coordinators])
    html = render_template("emails/contact_submitted.html", survey=survey,
                           user=current_user)
    msg.html = html
    msg.body = striptags(html)
    mail.send(msg)
