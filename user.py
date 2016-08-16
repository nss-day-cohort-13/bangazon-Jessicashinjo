import pickle
import uuid
from service_functions import *

class User:

  def __init__(self, user_name, user_screen_name):
    self.user_id = generate_uuid()
    self.full_name = user_name
    self.screen_name = user_screen_name
    self.user_data = {
                      "user_uuid": self.user_id,
                      "user_name": self.full_name,
                      "user_screen_name": self.screen_name
                      }
    serialize("user_data.txt", self.user_data)

  # def delete_user(self):
    # pass


# if __name__ == '__main__':
  # User("James Jones", "KillBill")
  # User("Juniper Jones", "JJPop")
  # User("Flipity Flop", "Fidyldydo")
  # deserialize("user_data.txt")
