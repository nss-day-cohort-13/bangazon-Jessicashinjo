import unittest
from birdyboard import *

class TestBirdyBoard(unittest.TestCase):


    @classmethod
    def set_up(self):
      self.birdyboard = Birdyboard()
      self.message = [88, "Juniper Jones", "public", "Jessie Jones", "chirpity chirp mate"]
      self.write_message = birdyboard.write_chirp(self.message)
      self.delete_message = birdyboard.delete_chirp(self.message)
      # self.read_message = birdyboard.read_chirp()

    def test_new_user_is_a_dictionary(self):
      self.assertEqual(self.birdyboard.create_user("Juniper Jones", "birdistheword"), [79, "Juniper Jones", "birdistheword"])

    def test_chirp_is_written_to_chirps_file(self):
      self.write_message
      self.assertIn(self.message,'chirps.csv')
      self.delete_message

    def test_chirp_is_removed_from_chirps_file(self):
      self.write_message
      self.delete_message
      self.assertNotIn(self.message, 'chirps.csv')

    def test_view_chirps_returns_chirps(self):
      self.write_message
      message_list = birdyboard.read_chirps()
      self.delete_message
      self.assertTrue(message_list == [str])

    # def test_private_chirp_is_private(self):
    #   pass


if __name__ == '__main__':
  unittest.main()

#########################################
##           Birdyboard~~~~~           ##
#########################################
# 1. New User Account
# 2. Select User
# 3. View Chirps
# 4. Public Chirp
# 5. Private Chirp
# 6. Exit


# Tests to write first round
# test_user_is_created
# test_chirp_is_written_to_chirps_file
# test_view_chirps_shows_chirps
# test_private_chirp_is_private

# Do I test these things or just deal with exception handling?
# If full_name or user_name input is empty
# userID creation
