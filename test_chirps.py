import unittest
from chirps import *


class TestChirps(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.chirps = Chirps()
    self.testable_public_chirp = self.chirps.create_public_chirp("14e234r2341", "If you have Monochromacy colorblindness can you truely understand color?")
    self.testable_private_chirp = self.chirps.create_private_chirp("14e234r2341", "Juniper Jones", "Yer pants are on fire mate")
    # self.testable_private_chirp = self.chirps.create_private_chirp(user_id, full_name, screen_name, to_whom, message)
    self.read_public_chirps = self.chirps.read_public_chirps()
    self.read_private_chirps = self.chirps.read_private_chirps()

    def tearDown(self):
      # Delete the test chirps from the chirps.txt file
      pass

  def test_public_chirp_is_written_to_chirps_file_with_chirp_id(self):
    chirps = self.read_public_chirps
    chirp_list = []
    chirp_id = []
    for specific_chirp in chirps:
      chirp_list.append(specific_chirp["chirp_message"])
      chirp_id.append(chirp_name["chirp_uuid"])
    # print("chirps List", chirp_list)
    self.assertIn("If you have Monochromacy colorblindness can you truely understand color?", chirp_list)
    self.assertNotIn('', chirp_id)

  def test_public_chirps_are_public(self):
    chirps = self.read_public_chirps
    for specific_chirp in chirps:
      self.assertTrue(specific_chirp["public"])

  def test_private_chirp_is_written_to_chirps_file_with_chirp_id(self):
    chirps = self.read_private_chirps
    chirp_list = []
    chirp_id = []
    for specific_chirp in chirps:
      chirp_list.append(specific_chirp["chirp_message"])
      chirp_id.append(chirp_name["chirp_uuid"])
    # print("chirps List", chirp_list)
    self.assertIn("Yer pants are on fire mate", chirp_list)
    self.assertNotIn('', chirp_id)

  def test_private_chirps_are_private(self):
    chirps = self.read_private_chirps
    for specific_chirp in chirps:
      self.assertTrue(specific_chirp["public"])

  # def test_chirp_is_removed_from_chirps_file(self):
  #   self.write_message
  #   self.delete_message
  #   self.assertNotIn(self.message, 'chirps.csv')

  def test_view_chirps_returns_chirps(self):
    self.write_message
    message_list = birdy.read_chirps()
    self.delete_message
    self.assertTrue(message_list == [str])



if __name__ == '__main__':
    unittest.main()
