import unittest
from user import *


class Test_User(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.user = User()

  def tearDown(self):
    # Delete the test user from user_data.txt file
    pass

  def test_new_user_is_in_user_data_file_with_id_that_is_not_empty_string(self):
    ''' This test calls the create_user function to ensure that our test user
    is in the file being tested. Then it reads the users in the file and adds
    every user's name to a list. Then assertIn asserts that the test user's name
    is in the list of user's names.'''

    self.user.create_user("Juniper Jones", "birdistheword")
    users = self.user.read_users()
    user_list = []
    user_id = []
    for user_name in users:
      user_list.append(user_name["user_name"])
      user_id.append(user_name["user_uuid"])
    # print("users List", user_list)
    self.assertIn("Juniper Jones", user_list)
    self.assertNotIn('', user_id)

  # def test_user_has_id(self):
  #   pass

if __name__ == '__main__':
    unittest.main()
