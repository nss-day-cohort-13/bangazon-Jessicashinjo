import unittest


class Test_User(unittest.TestCase):

  @classmethod
  def setUpClass(self):

  def test_new_user_is_in_user_data_file(self):
    self.birdy.create_user("Juniper Jones", "birdistheword")
    users = self.birdy.read_users()
    user_data = [users]
    self.assertIn("Juniper Jones", user_data)

if __name__ == '__main__':
    unittest.main()
