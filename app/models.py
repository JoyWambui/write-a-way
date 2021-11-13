from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    """Class that defines the User Model and its methods."""
    __tablename__='users'
    
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(25), unique=True,nullable=False)
    user_email = db.Column(db.String(120), unique=True,nullable=False)
    user_password = db.Column(db.String(255), unique=True,nullable=False)
    #Setting password and its hash
    @property
    def password(self):
        raise AttributeError('This attribute cannot be accessed.')
    
    @password.setter
    def password(self,password):
        self.user_password = generate_password_hash(password)
    
    def verify_password_hash(self,password):
        return check_password_hash(self.user_password,password)
    
    #user_bio = db.Column(db.String(25), unique=True,nullable=False)
    #image= db.Column(db.String(25), unique=True,nullable=False)
    #user_posts= db.relationship('Post',backref='author',lazy=True)
    def __repr__(self):
        return f"User('{self.username}','{self.user_email}')"
    
# class Post(db.Model):
#     """Class that defines the Blog Post Model and its methods."""
#     __tablename__='posts'
    
#     id = db.Column(db.Integer,primary_key=True)
#     post_title= db.Column(db.String(60),nullable=False)
#     post_content= db.Column(db.Text,nullable=False)
#     post_creation = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
#     def __repr__(self):
#         return f"Post('{self.post_title}','{self.post_creation}')"