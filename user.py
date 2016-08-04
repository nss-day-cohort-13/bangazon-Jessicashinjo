import pickle
import uuid

class User():

  def __init__(self):
    self.users_deserialized = []

  def create_user(self, full_name, screen_name):
    ''' Takes arguments of the user's full name and the user's screen name:

    Checks to see if user_data file exists. If the file does not exist
    it will create the file and add the user. If it does exist, it will read
    the user_data file to see if user exists. If the user exists there will
    be an error thrown. If the user does not exist, it will generate a user_id
    and he or she will be added to the csv file with the user_id, full_name,
    and screen_name.
    '''
    try:
      self.read_users()

    except:
      pass


    with open("user_data.txt", "wb+") as pickle_file:
      user_id = str(uuid.uuid4())

      user_data = {
        "user_uuid": user_id,
        "user_name": full_name,
        "user_screen_name": screen_name
      }

      self.users_deserialized.append(user_data)
      # print(self.users_deserialized)

      pickle.dump(self.users_deserialized, pickle_file)

      # if I try to read users before uses exist I get a an EOFError "ran out of input"
    # try:
        # user.read_users()
    # except EOFError as e:
    #   raise

  def read_users(self):
    with open("user_data.txt", "rb+") as pickle_file:
      self.users_deserialized = pickle.load(pickle_file)

    print(self.users_deserialized)
    return self.users_deserialized


if __name__ == '__main__':
  user = User()
  # user.read_users()
  user.create_user("Joe", "Joeydoughy")
