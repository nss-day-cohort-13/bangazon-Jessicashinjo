import pickle
import uuid
from user import *
from chirps import *
from service_functions import *

# class PrivateChirps():
#   def __init__(self, user_id, user_screen_name, message):
class PrivateChirps(Chirps):
  def __init__(self, user_id, user_screen_name, message, receiver_id, receiver_screen_name):
    Chirps.__init__(self, user_id, user_screen_name, message)
    # self.current_time = time()
    # self.timestamp = datetime.fromtimestamp(self.current_time).strftime('%Y-%m-%d %H:%M:%S')
    # self.chirp_id = generate_uuid()
    # self.user_uuid = user_id
    # self.screen_name = user_screen_name
    # self.message = message
    self.storage_file = "private_chirps.txt"
    self.public = False
    self.receiver_id = receiver_id
    self.receiver_screen_name = receiver_screen_name
    self.private_chirp_data = {
            "user_uuid": self.user_uuid,
            "user_screen_name": self.screen_name,
            "chirp_uuid": self.chirp_id,
            "public": self.public,
            "message": self.message,
            "timestamp": self.timestamp,
            "receiver_id": self.receiver_id,
            "receiver_screen_name": self.receiver_screen_name
            }
    serialize(self.storage_file, self.private_chirp_data)






# def create_private_chirp(self, screen_name, send_to_screen_name, message):
#   ''' Takes arguments of the user's full name, screen name, if it should be
#       public or private, who the chirp will be sent to, and the message
#       itself:
#
#   Opens user_data and searches for user. If the file does not contain user,
#   throws an error to sign up and sends user back to the menu. If it does
#   contain user it will close the file and open the chirps file. Next it will
#   check the privacy. If privacy is public it will generate a chirp_id
#   and write the chirp_id, full_name, screen_name, privacy, to_whom
#   (automatically listed as "public" if privacy is public), and message to the
#   chirps.csv file.
#   '''
#
#   with open("private_chirps.txt", "wb+") as pickle_file:
#     chirp_id = str(uuid.uuid4())
#     user_id = str
#     receiver_id = str
#     current_time = time()
#     timestamp = datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')
#     for each_user in self.user.read_users():
#       # print("Each User", each_user)
#       if screen_name == each_user["user_screen_name"]:
#         # print("You made it this far mate")
#         user_id = each_user["user_uuid"]
#       if send_to_screen_name == each_user["user_screen_name"]:
#         receiver_id = each_user["user_uuid"]
#       else:
#         print("User not found")
#         print("user is", each_user["user_screen_name"])
#
#         chirp_data = {
#           "sender_uuid": user_id,
#           "sender_screen_name": screen_name,
#           "chirp_uuid": chirp_id,
#           "receiver_uuid": receiver_id,
#           "receiver_screen_name": send_to_screen_name,
#           "public": False,
#           "message": message,
#           "timestamp": timestamp # sort by timestamp using sorted()
#         }
#
#         self.private_chirps_deserialized.append(chirp_data)
#         # print(self.private_chirps_deserialized)
#         pickle.dump(self.private_chirps_deserialized, pickle_file)
#
# def read_private_chirps(self, screen_name):
#   user_messages = []
#       try:
#       except:
#         pass
#   with open("private_chirps.txt", "rb+") as pickle_file:
#     self.private_chirps_deserialized = pickle.load(pickle_file)
#     private_messages = self.private_chirps_deserialized
#     print("private messages", private_messages)
#     for user in private_messages:
#       if screen_name == user["sender_screen_name"] | user["receiver_screen_name"]:
#         message = {
#           "receiver_id": user["receiver_uuid"],
#           "receiver": user["receiver_screen_name"],
#           "message": user["message"],
#           "sender_id": user["sender_uuid"],
#           "sender": user["sender_screen_name"],
#           "chirp_id": user["chirp_uuid"],
#           "privacy": user["public"],
#           "timestamp": user["timestamp"]
#         }
#         user_messages.append(message)
#   print(user_messages)
#   return user_messages
#
# def delete_private_chirp(self, screen_name, chirp_id):
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

  # for user in User.read_users():
  #   if self.user_uuid == user["user_uuid"]:


if __name__ == '__main__':
  PrivateChirps(86419575609614075990463230600833442718, 'check_yoself', "Do private chirps work?", 148483404200007806254540872871643687611, 'test_yoself')
  # chirps.create_public_chirp('JJPop', "Public service announcement yoooo")
  deserialize("chirps.txt")
  # chirps.create_private_chirp('JJPop', 'Fidyldydo', "Sushhhhhiiiiin")
  # chirps.read_private_chirps('JJPop')
