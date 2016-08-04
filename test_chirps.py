import unittest


class TestChirps(unittest.TestCase):

  @classmethod
  def setUpClass(self):

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
    message_list = birdy.read_chirps()
    self.delete_message
    self.assertTrue(message_list == [str])



if __name__ == '__main__':
    unittest.main()
