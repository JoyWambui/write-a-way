from flask import render_template,redirect,url_for
from . import auth
from ..models import User
from .. import db
from .forms import RegistrationForm

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