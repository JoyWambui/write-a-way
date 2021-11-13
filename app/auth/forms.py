from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo,Length
from ..models import User

class RegistrationForm(FlaskForm):
    sign_up_username = StringField('Input your Username:',validators=[InputRequired(message='This field is required.'),Length(min=5,max=20,message='Username should be between 5 and 20 characters.')])
    sign_up_email = StringField('Input your Email:',validators=[InputRequired('This field is required.'),Email(message='Input email in this format:username@gmail.com')])
    sign_up_password = PasswordField('Input your Password:',validators=[InputRequired('This field is required.'),EqualTo('confirm_password',message='Passwords must match'),Length(min=5,max=10,message='Password should be between 5 and 10 characters.')])
    confirm_password =PasswordField('Confirm input Password:',validators=[InputRequired('This field is required,')])
    sign_up_submit = SubmitField('Sign Up')
    
    def validate_email(self,data_field):
        if User.query.filter_by(sign_up_email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(sign_up_username=data_field.data).first():
            raise ValidationError('That username is taken.Choose another username')
        
class LoginForm(FlaskForm):
    login_email = StringField('Input your Email Adress:',validators=[InputRequired('This field is required.'),Email(message='Input email in this format:username@gmail.com')])
    login_password = PasswordField('Input your Password:',validators=[InputRequired('This field is required.')])
    remember_me =BooleanField('Remember me')
    login_submit = SubmitField('Log in')
