from crypt import methods
from flask import render_template,request,redirect,url_for,abort
from flask_login import current_user,login_required
from ..emails import mail_message
from app.request import get_quotes
from ..models import Post, User,Comment,Subscription
from . import main
from .forms import UpdateUserAccount,BlogPost,CommentForm,SubscriptionForm
from .. import db,images
import markdown2

@main.route('/')
def index():
    random_quote= get_quotes()
    print(random_quote)
    all_posts=Post.get_all_posts()
    title='Write_a_way'
    return render_template('index.html',all_posts=all_posts,title=title,random_quote=random_quote)

@main.route('/subscribe',methods=['GET','POST'])
def subscribe():
    subscription_form = SubscriptionForm()
    if subscription_form.validate_on_submit():
        name= subscription_form.subscribe_name.data
        email= subscription_form.subscribe_email.data
        subscriber= Subscription(name=name,email=email)
        db.session.add(subscriber)
        db.session.commit()
        return redirect(url_for('.index'))
    title='Subscribe'
    return render_template('subscribe.html', subscription_form=subscription_form,title=title)

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
        new_post.save_posts()
        subscribers = Subscription.query.all()
        for subscribe in subscribers:
            mail_message("New Post is up!","emails/new_post",subscribe.email,subscribe=subscribe)
        return redirect(url_for('.user_posts', username=username))
    
    title='Create New Post'
    return render_template('new_post.html', title=title,post_form=post_form)

@main.route('/user/<username>/posts')
@login_required
def user_posts(username):
    user=User.query.filter_by(username=username).first()
    user_posts = Post.get_user_posts(user.id)    
    title='My Posts'
    return render_template('posts.html', title=title,user_posts=user_posts)

@main.route('/posts/<int:id>')
def single_post(id):
    post=Post.query.get(id)
    if post is None:
        abort(404)
    format_post = markdown2.markdown(post.post_content,extras=["code-friendly", "fenced-code-blocks"])
    post_comments=Comment.get_post_comments(post.id)
    return render_template('post.html',post=post,format_post=format_post,post_comments=post_comments)

@main.route('/posts/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_post(id):
    post = Post.query.get(id)
    if post is None:
        abort(404)
    if post.author != current_user:
        abort(403)
    post_form= BlogPost()
    if post_form.validate_on_submit():
        post.post_title= post_form.added_post_title.data
        post.post_content = post_form.added_post_content.data
        db.session.commit()
        return redirect(url_for('.single_post', id=post.id))
    elif request.method == 'GET':
        post_form.added_post_title.data=post.post_title
        post_form.added_post_content.data = post.post_content
    title='Update Post'
    return render_template('new_post.html', title=title,post_form=post_form)

@main.route('/posts/<int:id>/delete', methods=['GET','POST'])
@login_required
def delete_post(id):
    post = Post.query.get(id)
    if post is None:
        abort(404)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('.index'))

@main.route('/posts/<int:id>/comment/new',methods=['GET','POST'])
def new_comment(id):
    post=Post.query.get(id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(comment_title=comment_form.added_comment_title.data,comment_author=comment_form.added_comment_author.data,comment_content=comment_form.added_comment_content.data,comment=post)
        new_comment.save_comment()
        return redirect(url_for('.single_post', id=post.id))
    
    title='Add a Comment'
    return render_template('new_comment.html', title=title,comment_form=comment_form)

@main.route('/comments/<int:id>/delete', methods=['GET','POST'])
@login_required
def delete_comment(id):
    comment = Comment.query.get(id)
    if comment is None:
        abort(404)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('.single_post', id=comment.post_id))


