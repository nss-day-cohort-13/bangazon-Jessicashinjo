import pickle
import uuid
from user import *

class Chirps():
  def __init__(self):
    self.public_chirps_deserialized = []
    self.user = User()

  def create_public_chirp(self, user_id, message):
    sender = list()
    try:
      users = self.read_public_chirps()
      for each_user in users:
        if user_id == each_user[user_id]:
          sender.append(each_user)
      print("The sender is: ", sender)

    except:
      pass

    with open("public_chirps.txt", "wb+") as pickle_file:
      chirp_id = str(uuid.uuid4())
      screen_name = str
      for user in sender:
        if user_id == user["user_uuid"]:
          screen_name = user["user_screen_name"]

      chirp_data = {
        "user_uuid": user_id,
        # "user_name": full_name,
        "user_screen_name": screen_name,
        "public": True,
        "message": message
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

  def create_private_chirp(self, user_id, full_name, screen_name, privacy, to_whom, message):
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

    pass
    try:
      self.read_chirps()

    except:
      pass

    with open("chirps.txt", "wb+") as pickle_file:
      chirp_id = str(uuid.uuid4())

      chirp_data = {
        "user_uuid": user_id,
        "user_name": full_name,
        "user_screen_name": screen_name
      }

      self.users_deserialized.append(user_data)
      pickle.dump(self.users_deserialized, pickle_file)


  def read_private_chirps(self, screen_name):
    pass

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
  chirps.create_public_chirp("86e3298d-2e3e-4a26-9cba-fcdd97eefd29", "awwwww yeaaaaa")
