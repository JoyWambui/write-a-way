import imp
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import InputRequired,Length,Email

class UpdateUserAccount(FlaskForm):
    added_user_bio = TextAreaField('Tell us a little about you',validators=[InputRequired()])
    bio_submit = SubmitField('Add bio')
    
class BlogPost(FlaskForm):
    added_post_title = StringField('Input Blog Post Title:',validators=[InputRequired(),Length(min=5,max=60)])
    added_post_content= TextAreaField('Write Your Post:')
    submit = SubmitField('Add Post')
    
class CommentForm(FlaskForm):
    added_comment_title = StringField('Input Comment Title:',validators=[InputRequired(),Length(min=5,max=60)])
    added_comment_author = StringField('Input Your Name:',validators=[InputRequired(),Length(max=60)])
    added_comment_content= TextAreaField('Write Your Comment:')
    comment_submit = SubmitField('Add Comment')

class SubscriptionForm(FlaskForm):
    subscribe_name = StringField('Input your Name:',validators=[InputRequired(message='This field is required.'),Length(max=20,message='Username should be under 20 characters.')])
    subscribe_email = StringField('Input your Email:',validators=[InputRequired('This field is required.'),Email(message='Input email in this format:username@gmail.com')])
    subscribe_submit = SubmitField('Subscribe')
