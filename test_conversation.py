from user import *
from chirps import *
from private_chirps import *
from conversation import *
import unittest
from service_functions import *

class TestConversation(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.test_user_1 = User("Snow Flake", "blizzard")
    self.test_user_2 = User("Butter Flies", "icky")
    self.public_chirp = Chirps(self.test_user_1.user_id, self.test_user_1.screen_name, "The sky is falling!")
    self.private_chirp = PrivateChirps(self.test_user_2.user_id, self.test_user_2.screen_name, "The sky is falling!", self.test_user_1.user_id, self.test_user_1.screen_name)
    self.public_conversation = Conversations(self.test_user_1.user_id, self.public_chirp.chirp_id, 0)
    self.private_conversation = Conversations(self.test_user_2.user_id, self.private_chirp.chirp_id, self.test_user_1.user_id)

  def test_public_conversation_creation(self):
    self.assertEqual(self.public_conversation.user_UUID, self.test_user_1.user_id)
    self.assertEqual(self.public_conversation.chirp_UUID, self.public_chirp.chirp_id)
    self.assertEqual(self.public_conversation.receiver_UUID, 0)
    self.assertIsNotNone(self.public_conversation.conversation_UUID)

  def test_private_conversation_creation(self):
    self.assertEqual(self.private_conversation.user_UUID, self.private_chirp.user_uuid)
    self.assertEqual(self.private_conversation.chirp_UUID, self.private_chirp.chirp_id)
    self.assertEqual(self.private_conversation.receiver_UUID, self.test_user_1.user_id)
    self.assertIsNotNone(self.private_conversation.conversation_UUID)


  # conversation_reply

  # List conversation replies by line number


if __name__ == '__main__':
    unittest.main()
