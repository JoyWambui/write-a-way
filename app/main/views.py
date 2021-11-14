from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from ..models import User
from . import main
from .forms import UpdateUserAccount
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def account(username):
    user=User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    title='Your Account'
    return render_template('account/account.html', title=title,user=user)

@main.route('/user/<username>/update', methods=['GET','POST'])
@login_required
def update_account(username):
    user=User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    bio_form= UpdateUserAccount()
    if bio_form.validate_on_submit():
        user.user_bio= bio_form.added_user_bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.account',username= user.username))
    
    title='Update Account'
    return render_template('account/account_update.html', title=title,bio_form=bio_form)
