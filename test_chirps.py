import unittest
from chirps import *
from user import *
from service_functions import *


class TestChirps(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.first_user = User("Test User 1", "test_yoself")
    self.second_user = User("Test User 2", "check_yoself")
    self.test_chirp_one = Chirps(self.first_user.user_id, "test_yoself", "If you have Monochromacy colorblindness can you truely understand color?")
    self.test_chirp_two = Chirps(self.second_user.user_id, "check_yoself", "Calm and simplicity.")
    # self.testable_public_chirp = PublicChirps("test_yoself", "check_yoself", "Yer pants are on fire mate")
    # self.read_public_chirps = PublicChirps.read_public_chirps()

  def tearDown(self):
    # Delete the test chirps from the chirps.txt file
    pass

  def test_public_chirp_creation(self):
    self.assertEqual(self.first_user.user_id, self.test_chirp_one.user_uuid)
    self.assertEqual("If you have Monochromacy colorblindness can you truely understand color?", self.test_chirp_one.message)
    self.assertEqual(self.first_user.screen_name, self.test_chirp_one.screen_name)
    self.assertEqual(True, self.test_chirp_one.public)

  def test_public_chirp_is_in_chirps_file(self):
    chirps = deserialize("chirps.txt")
    chirp_list = []
    for chirp in chirps:
      chirp_list.append(chirp.message)
      chirp_list.append(chirp.chirp_id)
    self.assertIn("If you have Monochromacy colorblindness can you truely understand color?", chirp_list)
    self.assertIsNotNone(self.test_chirp_one.chirp_id)

  # def test_chirp_is_removed_from_chirps_file(self):
  #   self.write_message
  #   self.delete_message
  #   self.assertNotIn(self.message, 'chirps.csv')



if __name__ == '__main__':
    unittest.main()
