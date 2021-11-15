from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
class User(UserMixin,db.Model):
    """Class that defines the User Model and its methods."""
    __tablename__='users'
    
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(25), unique=True,nullable=False)
    user_email = db.Column(db.String(120), unique=True,nullable=False)
    user_password = db.Column(db.String(255), unique=True,nullable=False)
    user_bio = db.Column(db.Text(),nullable=True)
    user_account_image= db.Column(db.String(),nullable=True)
    user_posts= db.relationship('Post',backref='author',lazy=True)

    #Setting password and its hash
    @property
    def password(self):
        raise AttributeError('This attribute cannot be accessed.')
    
    @password.setter
    def password(self,password):
        self.user_password = generate_password_hash(password)
    
    def verify_password_hash(self,password):
        return check_password_hash(self.user_password,password)
        
    def __repr__(self):
        return f"User('{self.username}','{self.user_email}')"
    
class Post(db.Model):
    """Class that defines the Blog Post Model and its methods."""
    __tablename__='posts'
    
    id = db.Column(db.Integer,primary_key=True)
    post_title= db.Column(db.String(60),nullable=False)
    post_content= db.Column(db.Text,nullable=False)
    post_creation = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    post_comments= db.relationship('Comment',backref='comment',lazy=True)
    def __repr__(self):
        return f"Post('{self.post_title}','{self.post_creation}')"
    
    def save_posts(self):
        """Saves new posts to the database."""
        db.session.add(self)
        db.session.commit()
    
    @classmethod    
    def get_user_posts(self,id):
        """Gets all a user's posts."""
        got_posts= Post.query.filter_by(user_id=id).all()
        return got_posts
    
    @classmethod    
    def get_all_posts(self):
        """Gets all posts."""
        all_posts= Post.query.all()
        return all_posts
    
class Comment(db.Model):
    """Class that defines the Comment Model and its methods."""
    __tablename__='comments'
    
    id = db.Column(db.Integer,primary_key=True)
    comment_title= db.Column(db.String(60),nullable=False)
    comment_author= db.Column(db.String(60),nullable=False)
    comment_content= db.Column(db.Text,nullable=False)
    comment_creation = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'),nullable=False)
