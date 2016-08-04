import unittest
from user import *


class Test_User(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.user = User()

  def test_new_user_is_in_user_data_file(self):
    self.user.create_user("Juniper Jones", "birdistheword")
    users = self.user.read_users()
    user_data = [users]
    self.assertIn("Juniper Jones", user_data)

if __name__ == '__main__':
    unittest.main()
