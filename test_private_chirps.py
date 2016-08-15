import unittest
from chirps import *
from private_chirps import *
from user import *
from service_functions import *


class TestChirps(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.first_user = User("Blue Potatoes", "chips")
    self.second_user = User("Orange Bananas", "juice")
    self.test_chirp_one = PrivateChirps(self.first_user.user_id, "chips", "Quote of the day", self.second_user.user_id, "juice")
    # self.test_chirp_two = PrivateChirps(self.second_user.user_id, "check_yoself", "Calm and simplicity.")

  def tearDown(self):
    # Delete the test chirps from the chirps.txt file
    pass

  def test_private_chirp_creation(self):
    self.assertEqual(self.first_user.user_id, self.test_chirp_one.user_uuid)
    self.assertEqual(self.first_user.screen_name, self.test_chirp_one.screen_name)
    self.assertEqual("Quote of the day", self.test_chirp_one.message)
    self.assertEqual(self.second_user.user_id, self.test_chirp_one.receiver_id)
    self.assertEqual("juice", self.test_chirp_one.receiver_screen_name)
    self.assertFalse(self.test_chirp_one.public)

  def test_private_chirp_is_in_chirps_file(self):
    chirps = deserialize("private_chirps.txt")
    chirp_list = []
    for chirp in chirps:
      chirp_list.append(chirp["user_uuid"])
      chirp_list.append(chirp["user_screen_name"])
      chirp_list.append(chirp["chirp_uuid"])
      chirp_list.append(chirp["public"])
      chirp_list.append(chirp["message"])
      chirp_list.append(chirp["receiver_id"])
      chirp_list.append(chirp["receiver_screen_name"])
    # print("chirps List", chirp_list)
    self.assertIn(self.test_chirp_one.user_uuid, chirp_list)
    self.assertIn("chips", chirp_list)
    # self.assertFalse("chips", chirp_list)
    self.assertIn("Quote of the day", chirp_list)
    self.assertIn("juice", chirp_list)
    self.assertIn(self.second_user.user_id, chirp_list)
    self.assertIsNotNone(self.test_chirp_one.private_chirp_id)

  # def test_chirp_is_removed_from_chirps_file(self):
  #   self.write_message
  #   self.delete_message
  #   self.assertNotIn(self.message, 'chirps.csv')



if __name__ == '__main__':
    unittest.main()
