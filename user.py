import pickle
import uuid

class User:

  def __init__(self, user_name, user_screen_name):
    self.user_id = uuid.uuid4().int
    self.full_name = user_name
    self.screen_name = user_screen_name
    self.user_data = {
                      "user_uuid": self.user_id,
                      "user_name": self.full_name,
                      "user_screen_name": self.screen_name
                      }
    self.create_user()

  def create_user(self):
    ''' Takes arguments of the user's full name and the user's screen name:

    Checks to see if user_data file exists. If the file does not exist
    it will create the file and add the user. If it does exist, it will read
    the user_data file to see if user exists. If the user exists there will
    be an error thrown. If the user does not exist, it will generate a user_id
    and he or she will be added to the csv file with the user_id, full_name,
    and screen_name.
    '''
    ##########################################################################
    # Write code to check for existing users or errors will rain down upon you
    ##########################################################################

    with open("user_data.txt", "ab+") as pickle_file:
      pickle.dump(self.user_data, pickle_file)

  @staticmethod
  def read_users():
    """ """
    users_deserialized = []
    with open("user_data.txt", "rb") as pickle_file:
      while True:
        try:
            users_deserialized.append(pickle.load(pickle_file))
        except FileNotFoundError:
          print("I'm a potato!")
        except EOFError:
          break

      print(users_deserialized)
      return users_deserialized

  # def delete_user(self):
    # pass


# if __name__ == '__main__':
  # User("Juniper Jones", "JJPop")
  # User.read_users()
  # User("Flipity Flop", "Fidyldydo")
