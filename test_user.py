import unittest
from user import *


class Test_User(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.user = User()

  def test_new_user_is_in_user_data_file(self):
    ''' This test calls the create_user function to ensure that our test user
    is in the file being tested. Then it reads the users in the file and adds
    every user's name to a list. Then assertIn asserts that the test user's name
    is in the list of user's names. Once finished the test will delete the test
    name from the file '''
    
    self.user.create_user("Juniper Jones", "birdistheword")
    users = self.user.read_users()
    user_list = []
    for user_name in users:
      user_list.append(user_name["user_name"])
    # print("users List", user_list)
    self.assertIn("Juniper Jones", user_list)

if __name__ == '__main__':
    unittest.main()
