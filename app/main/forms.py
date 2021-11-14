import imp
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import InputRequired

class UpdateUserAccount(FlaskForm):
    added_user_bio = TextAreaField('Tell us a little about you',validators=[InputRequired()])
    bio_submit = SubmitField('Add bio')