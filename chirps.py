import pickle
import uuid
from datetime import datetime
from time import time
from user import *

class Chirps():
  def __init__(self):
    self.public_chirps_deserialized = []
    self.private_chirps_deserialized = []
    self.user = User()

  # Passed in screen_name vs uuid because screen_name was easier to test
  def create_public_chirp(self, screen_name, message):
    try:
      self.read_public_chirps()
    except EOFError:
      pass

    except FileNotFoundError:
      print("i'm a duck")


    with open("public_chirps.txt", "wb+") as pickle_file:
      chirp_id = str(uuid.uuid4())
      user_id = str
      current_time = time()
      timestamp = datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')
      for each_user in self.user.read_users():
        # print("Each User", each_user)
        if screen_name == each_user["user_screen_name"]:
          # print("You made it this far mate")
          user_id = each_user["user_uuid"]
        else:
          pass
          # Throw exception "user not found"
          # print("user is", each_user["user_screen_name"])

      chirp_data = {
        "user_uuid": user_id,
        "user_screen_name": screen_name,
        "chirp_uuid": chirp_id,
        "public": True,
        "message": message,
        "timestamp": timestamp
      }

      self.public_chirps_deserialized.append(chirp_data)
      pickle.dump(self.public_chirps_deserialized, pickle_file)

  def read_public_chirps(self):
    ''' Takes the user's screen_name as its argument:

    Opens user_data.csv file and searches for the screen_name. If the
    screen_name does not exist it will only print public chirps. If the
    screen_name does exist it will print public and the user's private chirps in
    separate sections.
    '''
    with open("public_chirps.txt", "rb+") as pickle_file:
      self.public_chirps_deserialized = pickle.load(pickle_file)

      print(self.public_chirps_deserialized)
      return self.public_chirps_deserialized

  def create_private_chirp(self, screen_name, send_to_screen_name, message):
    ''' Takes arguments of the user's full name, screen name, if it should be
        public or private, who the chirp will be sent to, and the message
        itself:

    Opens user_data and searches for user. If the file does not contain user,
    throws an error to sign up and sends user back to the menu. If it does
    contain user it will close the file and open the chirps file. Next it will
    check the privacy. If privacy is public it will generate a chirp_id
    and write the chirp_id, full_name, screen_name, privacy, to_whom
    (automatically listed as "public" if privacy is public), and message to the
    chirps.csv file.
    '''
    try:
      users = self.read_private_chirps()
    except:
      pass


    with open("private_chirps.txt", "wb+") as pickle_file:
      chirp_id = str(uuid.uuid4())
      user_id = str
      receiver_id = str
      current_time = time()
      timestamp = datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')
      for each_user in self.user.read_users():
        # print("Each User", each_user)
        if screen_name == each_user["user_screen_name"]:
          # print("You made it this far mate")
          user_id = each_user["user_uuid"]
        if send_to_screen_name == each_user["user_screen_name"]:
          receiver_id = each_user["user_uuid"]
        else:
          print("User not found")
          print("user is", each_user["user_screen_name"])

          chirp_data = {
            "sender_uuid": user_id,
            "sender_screen_name": screen_name,
            "chirp_uuid": chirp_id,
            "receiver_uuid": receiver_id,
            "receiver_screen_name": send_to_screen_name,
            "public": False,
            "message": message,
            "timestamp": timestamp
          }

          self.private_chirps_deserialized.append(chirp_data)
          # print(self.private_chirps_deserialized)
          pickle.dump(self.private_chirps_deserialized, pickle_file)

  def read_private_chirps(self, screen_name):
    user_messages = []
    with open("private_chirps.txt", "rb+") as pickle_file:
      self.private_chirps_deserialized = pickle.load(pickle_file)
      private_messages = self.private_chirps_deserialized
      print("private messages", private_messages)
      for user in private_messages:
        if screen_name == user["sender_screen_name"]:
          message = {
            "receiver_id": user["receiver_uuid"],
            "receiver": user["receiver_screen_name"],
            "message": user["message"],
            "sender_id": user["sender_uuid"],
            "sender": user["sender_screen_name"],
            "chirp_id": user["chirp_uuid"],
            "privacy": user["public"],
            "timestamp": user["timestamp"]
          }
          user_messages.append(message)
    print(user_messages)
    return user_messages

  def delete_chirp(self, screen_name, chirp_id):
    ''' Takes arguments of the user's screen name and id of the message to be
        deleted:

    First it will open the user_data.csv and check to see if the owner of the
    chirp is the one deleting chirp. If the person deleting the chirp is not
    the owner, it will throw an error saying "You cannot delete another user's
    chirp". If the person deleting the chirp is the owner, it will remove the
    chirp (without asking "Are you sure?") and allow the user to continue to
    delete chirps until they are done.
    '''
    pass


if __name__ == '__main__':
  chirps = Chirps()
  # chirps.create_public_chirp('JJPop', "Public service announcement yoooo")
  chirps.read_public_chirps()
  # chirps.create_private_chirp('JJPop', 'Fidyldydo', "Sushhhhhiiiiin")
  # chirps.read_private_chirps('JJPop')
