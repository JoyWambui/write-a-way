from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from ..models import Post, User
from . import main
from .forms import UpdateUserAccount,BlogPost
from .. import db,images

@main.route('/')
def index():
    all_posts=Post.get_all_posts()
    title='Write_a_way'
    return render_template('index.html',all_posts=all_posts,title=title)

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

@main.route('/user/<username>/update/profile-picture', methods=['POST'])
@login_required
def update_profile_picture(username):
    user=User.query.filter_by(username=username).first()
    if 'image' in request.files:
        filename = images.save(request.files['image'])
        image_path = f'images/{filename}'
        user.user_account_image = image_path
        db.session.commit()        
        return redirect(url_for('.account',username= username))
    
@main.route('/user/<username>/posts/new', methods=['GET','POST'])
@login_required
def new_post(username):
    user=User.query.filter_by(username=username).first()
    post_form= BlogPost()
    if post_form.validate_on_submit():
        print(post_form.errors)
        new_post = Post(post_title=post_form.added_post_title.data,post_content=post_form.added_post_content.data,author=user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('.user_posts', username=username))
    
    title='Create New Post'
    return render_template('new_post.html', title=title,post_form=post_form)

@main.route('/user/<username>/posts/')
@login_required
def user_posts(username):
    user=User.query.filter_by(username=username).first()
    user_posts = Post.get_user_posts(user.id)    
    title='My Posts'
    return render_template('posts.html', title=title,user_posts=user_posts)
