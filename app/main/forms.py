import imp
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import InputRequired,Length

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
