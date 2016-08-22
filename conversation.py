import pickle
# from chirps import *
# from private_chirps import *
# from user import *
from service_functions import *

class Conversations:
  def __init__(self, user_id, chirp_id, receiver_id):
    self.user_UUID = user_id
    self.chirp_UUID = chirp_id
    self.receiver_UUID = receiver_id
    self.conversation_UUID = generate_uuid()
    self.timestamp = timestamp()

    serialize("conversations.txt", self)

# This file will have functions that look for the selected to user...

# if __name__ == '__main__':
#   Conversations(13545326246346, 46246546527)
#   deserialize("conversations.txt")
