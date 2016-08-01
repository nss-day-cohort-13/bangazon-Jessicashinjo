import unittest
from birdyboard import *

class TestBirdyBoard(unittest.TestCase):

    def test_new_user_is_a_dictionary(self):
      birdyboard = Birdyboard()
      self.assertEqual(birdyboard.create_user("Juniper Jones", "birdistheword"), {"userID": 79, "full_name": "Juniper Jones", "screen_name": "birdistheword"})

    # def test_new_user_is_in_user_data_txt_file(arg):
      # pass

    # def test_correct_user_is_selected(self):
    #   birdyboard = Birdyboard()
    #   self.assertEqual()

    def test_only_correct_user_and_public_chirps_are_shown(self):
      birdyboard = Birdyboard()

    def test_chirp_writes_to_public_file(self):
      pass

    def test_private_chirp_writes_to_correct_file_under_user(self):
      pass

    # def test_when_6_is_chosen_program_exits(self):
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
