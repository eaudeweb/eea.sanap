from flask.ext import wtf


class LoginForm(wtf.Form):

    username = wtf.TextField('User ID', validators=[wtf.validators.Required()])

    password = wtf.PasswordField('Password',
                                 validators=[wtf.validators.Required()])


class RegisterForm(wtf.Form):

    email = wtf.TextField('E-mail', validators=[wtf.validators.Email()])

    first_name = wtf.TextField('First Name', validators=[wtf.validators.Required()])

    last_name = wtf.TextField('Last Name', validators=[wtf.validators.Required()])

    phone_number = wtf.TextField('Phone Number')

    organisation = wtf.TextField('Organisation')
