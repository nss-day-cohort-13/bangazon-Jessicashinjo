import pickle
import uuid
from datetime import datetime
from time import time
from user import *
from service_functions import *

class Chirps:
  def __init__(self, user_id, user_screen_name, message):
    self.timestamp = timestamp()
    self.chirp_id = generate_uuid()
    self.user_uuid = user_id
    self.screen_name = user_screen_name
    self.message = message
    self.public = True
    self.storage_file = "chirps.txt"
    self.chirp_data = {
            "user_uuid": self.user_uuid,
            "user_screen_name": self.screen_name,
            "chirp_uuid": self.chirp_id,
            "public": self.public,
            "message": self.message,
            "timestamp": self.timestamp
            }
    serialize(self.storage_file, self.chirp_data)

  # def delete_public_chirp(self, screen_name, chirp_id):
  #   ''' Takes arguments of the user's screen name and id of the message to be
  #       deleted:
  #
  #   First it will open the user_data.csv and check to see if the owner of the
  #   chirp is the one deleting chirp. If the person deleting the chirp is not
  #   the owner, it will throw an error saying "You cannot delete another user's
  #   chirp". If the person deleting the chirp is the owner, it will remove the
  #   chirp (without asking "Are you sure?") and allow the user to continue to
  #   delete chirps until they are done.
  #   '''
  #   pass


if __name__ == '__main__':
  Chirps(1643865979, 'BoBoFoSho', "Sho blamaaaaa")
  # PublicChirps('JJPop', "Public service announcement yoooo")
  deserialize("chirps.txt")
