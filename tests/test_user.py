import imp
# import unittest
# from app.models import User

# class TestUserModel(unittest.TestCase):
#     """Tests the User Model and its methods."""
    
#     def setUp(self):
#         """Sets up a new user instance."""
#         self.new_user= User(username='rick',user_email='rick@gmail.com',user_password='birdman')
        
#     def test_attribute_values(self):
#         """Tests that User properties have values."""
#         self.assertTrue(self.new_user.username is not None)
#         self.assertTrue(self.new_user.user_email is not None)
#         self.assertTrue(self.new_user.user_password is not None)
        
#     def test_no_access_password(self):
#         """Tests that a user cannot access the password property"""
#         with self.assertRaises(AttributeError):
#             self.new_user.user_password
            
#     def test_password_hash(self):
#         """Tests that a user password is hashed and if passed is the same as the hashed password."""
#         self.assertTrue(self.new_user.verify_password_hash('birdman'))
        
    

        