import unittest
from birdyboard import *

class TestBirdyBoard(unittest.TestCase):

    @classmethod
    def setUpClass(self):
      self.birdy = Birdyboard()
      # self.message = [88, "Juniper Jones", "birdistheword", "public", "public", "chirpity chirp mate"]
      # self.write_message = birdy.write_chirp(self.message)
      # self.delete_message = birdy.delete_chirp(self.message)
      # self.read_message = birdy.read_chirp()







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
