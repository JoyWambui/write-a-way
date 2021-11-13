from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from . import auth
from ..models import User
from .. import db
from .forms import RegistrationForm,LoginForm

@auth.route('/registration', methods=['GET','POST'])
def register():
    registration_form= RegistrationForm()
    if registration_form.validate_on_submit():
        new_user = User(username=registration_form.sign_up_username.data,user_email=registration_form.sign_up_email.data,password=registration_form.sign_up_password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    title= 'New Account'
    return render_template('auth/register.html',registration_form=registration_form,title=title)

@auth.route('/login', methods=['GET','POST'])
def login():
    login_form= LoginForm()
    if login_form.validate_on_submit():
        logged_in_user = User.query.filter_by(user_email=login_form.login_email.data).first()
        if logged_in_user is not None and logged_in_user.verify_password_hash(login_form.login_password.data):
            login_user(logged_in_user,login_form.remember_me.data)
            return redirect(request.args.get('next')or url_for('main.index'))
        flash('Invalid email or password!')
    title= 'Writer Login'
    return render_template('auth/login.html',login_form=login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    login_user()
    return redirect(url_for('.index'))