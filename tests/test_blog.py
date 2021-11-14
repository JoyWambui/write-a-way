import unittest
from app.models import Post,User
from app import db

class TestPostModel(unittest.TestCase):
    """Tests the Post Model and its methods."""
    
    def setUp(self):
        """Sets up a new user and post instance."""
        self.new_user= User(username='rick',user_email='rick@gmail.com',password='birdman')
        self.new_post=Post(post_title='rick and morty',post_content='adventures in space',author=self.new_user)
    
    def tearDown(self):
        """Deletes all elements from the database after every test."""
        Post.query.delete()
        User.query.delete()  
        db.session.commit()  

    def test_check_instance_attributes(self):
        """Check if attribute values are correctly placed."""
        self.assertEquals(self.new_post.post_title,'rick and morty')
        self.assertEquals(self.new_post.post_content,'adventures in space')
        self.assertEquals(self.new_post.author,self.new_user)
        self.assertEquals(self.new_post.user_id,self.new_user.id)
        
    def test_save_posts(self):
        """Check if a post is saved."""
        self.new_post.save_posts()
        self.assertTrue(len(Post.query.all())>0)
    
    def test_get_user_posts(self):
        """Iest if a user's posts are returned."""
        self.new_post.save_posts()
        got_posts=Post.get_user_posts(self.new_post.user_id)
        self.assertTrue(len(got_posts)==1)
        
    def test_get_all_posts(self):
        """Iest if all posts are returned."""
        self.new_post.save_posts()
        second_user= User(username='morty',user_email='morty@gmail.com',password='birdman')
        self.second_post=Post(post_title='morty and rick',post_content='space adventures',author=second_user)
        self.second_post.save_posts()
        all_posts=Post.get_all_posts()
        self.assertTrue(len(all_posts)==2)


