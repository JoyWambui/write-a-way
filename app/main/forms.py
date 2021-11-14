import imp
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import InputRequired,Length

class UpdateUserAccount(FlaskForm):
    added_user_bio = TextAreaField('Tell us a little about you',validators=[InputRequired()])
    bio_submit = SubmitField('Add bio')
    
class BlogPost(FlaskForm):
    added_post_title = StringField('Input Blog Post Title:',validators=[InputRequired(),Length(min=5,max=60)])
    added_post_content= TextAreaField('Write Your Post:',validators=[InputRequired()])
    post_submit = SubmitField('Add Post')