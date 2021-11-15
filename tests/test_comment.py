import unittest
from app.models import Post,Comment,User
from app import db

class TestPostModel(unittest.TestCase):
    """Tests the Post Model and its methods."""
    db.session.rollback()
    def setUp(self):
        """Sets up a new user,post,comment instances."""
        self.new_user= User(username='picklerick',user_email='picklerick@gmail.com',password='birdman')
        self.new_post=Post(post_title='rick and morty',post_content='adventures in space',author=self.new_user)
        self.new_comment=Comment(comment_title='Good job',comment_author='Summer',comment_content='You did a good job',comment=self.new_post)

    def tearDown(self):
        """Deletes all elements from the database after every test."""
        Post.query.delete()
        User.query.delete()  
        Comment.query.delete()
        try:
            db.session.commit()
        except:
            db.session.rollback()

    def test_check_instance_attributes(self):
        """Check if attribute values are correctly placed."""
        self.assertEquals(self.new_comment.comment_title,'Good job')
        self.assertEquals(self.new_comment.comment_author,'Summer')
        self.assertEquals(self.new_comment.comment_content,'You did a good job')
        self.assertEquals(self.new_comment.comment,self.new_post)
        self.assertEquals(self.new_comment.post_id,self.new_post.id)
        
    def test_save_comment(self):
        """Check if a comment is saved."""
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
    
    def test_get_post_comments(self):
        """Test if a post's comments are returned."""
        self.new_comment.save_comment()
        got_comments=Comment.get_post_comments(self.new_comment.post_id)
        self.assertTrue(len(got_comments)==1)
