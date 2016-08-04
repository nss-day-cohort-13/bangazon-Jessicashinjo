import pickle
import uuid

  def create_user(self, full_name, screen_name):
    ''' Takes arguments of the user's full name and the user's screen name:

    Checks to see if user_data file exists. If the file does not exist
    it will create the file and add the user. If it does exist, it will read
    the user_data file to see if user exists. If the user exists there will
    be an error thrown. If the user does not exist, it will generate a user_id
    and he or she will be added to the csv file with the user_id, full_name,
    and screen_name.
    '''

    with open("user_data.txt", "ab+") as pickle_file:
      user_id = str(uuid.uuid4())

      user_data = {
        "user_uuid": user_id,
        "user_name": full_name,
        "user_screen_name": screen_name
      }
      pickle.dump(user_data, pickle_file)


    # try:
    # except Exception as e:
    #   raise

  def read_users(self):
    users_deserialized = []
    with open("user_data.txt", "rb+") as pickle_file:
      users_deserialized = pickle.load(pickle_file)

    print(users_deserialized)
    return users_deserialized


if __name__ == '__main__':
