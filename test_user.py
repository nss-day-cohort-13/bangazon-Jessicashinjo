import unittest
from user import *
from service_functions import *


class Test_User(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.test_user = User("Juniper Jones", "birdistheword")

  def tearDown(self):
    # Delete the test user from user_data.txt file
    pass

  def test_user_creation(self):
    self.assertIsNotNone(self.test_user.user_id)
    self.assertEqual(self.test_user.full_name, "Juniper Jones")
    self.assertEqual(self.test_user.screen_name, "birdistheword")

  def test_new_user_is_in_user_data_file(self):
    ''' This test calls the create_user function to ensure that our test user
    is in the file being tested. Then it reads the users in the file and adds
    every user's name to a list. Then assertIn asserts that the test user's name
    is in the list of user's names.'''


    users = deserialize("user_data.txt")
    user_data = []

    for user in users:
      user_data.append(user["user_uuid"])
      user_data.append(user["user_name"])
      user_data.append(user["user_screen_name"])
    # print("users List", user_list)
    self.assertIn(self.test_user.user_id, user_data)
    self.assertIn("Juniper Jones", user_data)
    self.assertIn("birdistheword", user_data)

  # def test_user_was_deleted(self):
  #   pass

if __name__ == '__main__':
    unittest.main()
