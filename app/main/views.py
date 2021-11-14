from flask import render_template,request,redirect,url_for,abort
from ..models import User
from . import main

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