from flask.ext import wtf
from sanap.models import User, slugify


class LoginForm(wtf.Form):

    username = wtf.TextField('User ID', validators=[wtf.validators.Required()])

    password = wtf.PasswordField('Password',
                                 validators=[wtf.validators.Required()])


class RegisterForm(wtf.Form):

    email = wtf.TextField('E-mail', validators=[wtf.validators.Required(),
                                                wtf.validators.Email()])

    first_name = wtf.TextField('First Name', validators=[wtf.validators.Required()])

    last_name = wtf.TextField('Last Name', validators=[wtf.validators.Required()])

    phone_number = wtf.TextField('Phone Number')

    organisation = wtf.TextField('Organisation')

    def validate_email(self, field):
        if User.objects.filter(email=field.data, invitee__exists=False, country__exists=True).count() > 0:
            raise wtf.ValidationError('User is already invited as country coordinator with Eionet Account')

    def save(self, user_invitee):
        defaults = self.data
        defaults['id'] = slugify('%s %s' % (self.data['first_name'],
                                            self.data['last_name']))
        defaults['invitee'] = user_invitee
        defaults['country'] = user_invitee.country
        user, created = User.objects.get_or_create(email=self.data['email'],
                                                   defaults=defaults)
        return user