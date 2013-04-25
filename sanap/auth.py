import base64
from functools import wraps
import datetime

from flask import (Blueprint, request, render_template, redirect, url_for,
                   flash, g, abort)
from flask.ext.login import LoginManager
from flask.ext import wtf
from flask.ext import login as flask_login


from sanap.forms import LoginForm, RegisterForm
from sanap.models import User
from sanap import plugldap


auth = Blueprint('auth', __name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def login_required(fn):
    @wraps(fn)
    @flask_login.login_required
    def decorated_view(*args, **kwargs):
        if not g.user.country:
            return redirect(url_for('auth.unauthorized'))
        return fn(*args, **kwargs)
    return decorated_view


def load_user_in_g():
    g.user = flask_login.current_user


def initialize_app(app):
    app.register_blueprint(auth)
    app.before_request(load_user_in_g)


def get_user(userid):
    ''' Get or create user document in local db, using info in LDAP '''
    try:
        return User.objects.get(id=userid)
    except User.DoesNotExist:
        user_info = plugldap.user_info(userid)
        if user_info:
            (user, created) = User.objects.get_or_create(id=user_info['uid'],
                                                         defaults=user_info)
            return user
        else:
            return None
login_manager.user_loader(get_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username, password = request.form['username'], request.form['password']
        if plugldap.login_user(username, password):
            user = get_user(username)
            flask_login.login_user(user)
            flash('Logged in successfully as %s %s (%s).' %
                  (user.first_name, user.last_name, user.id))
            user.last_login = datetime.datetime.utcnow()
            user.save(safe=False)
            resp = redirect(request.args.get('next') or url_for('library.home'))
            resp.set_cookie('__ac',
                            base64.b64encode('%s:%s' % (username, password)))
            return resp
        else:
            flash('Bad username or password.')
    return render_template('login.html', form=form)


@auth.route('/access/<string:token>', methods=['GET', 'POST'])
def register(token):
    if g.user.is_authenticated():
        return redirect(url_for('survey.home'))
    try:
        user_invitee = User.objects.get(token=token)
    except User.DoesNotExist:
        flash(('Your access link appears to be incorrect.'
               ' Please make you sure you copied the full URL.'))
        return redirect(url_for('.unauthorized'))

    form = RegisterForm()
    if form.validate():
        user = form.save(user_invitee=user_invitee)
        flask_login.login_user(user)
        return redirect(url_for('survey.edit'))

    return render_template('register.html', form=form)


@auth.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    flash('You have successfully logged out.')
    resp = redirect(url_for('survey.home'))
    resp.set_cookie('__ac', '')
    return resp


@auth.route('/invite')
@login_required
def invite():
    if not g.user.token or g.user.invite:
        abort(403)
    return render_template('invite.html')


@auth.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html')
