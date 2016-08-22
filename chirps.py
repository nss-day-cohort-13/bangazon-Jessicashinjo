from service_functions import *

class Chirps:
  def __init__(self, user_id, user_screen_name, message, storage_file='chirps.txt', public=True):
    """ Creates a new public chirp

    Arguments:
    ----------
    user_id(int) = id of user creating the chirp
    user_screen_name(str) = screen name of the user creating the chirp
    message(str) = content of the user's message
    storage_file(str) = file which holds the serialized deserialized_data
    public(bool) = True if the chirp is public
    """
    self.timestamp = timestamp()
    self.chirp_id = generate_uuid()
    self.user_uuid = user_id
    self.screen_name = user_screen_name
    self.message = message
    self.public = public
    print("self", self)
    serialize(storage_file, self)

  def __str__(self):
    return self.message


# if __name__ == '__main__':
#   chirp = Chirps(1643865979, 'BoBoFoSho', "Sho blamaaaaa")
  # Chirps(432626436243, 'JJPop', "Public service announcement yoooo")
  # result = deserialize("chirps.txt")
  # for item in result:
  #     print(item.__dict__)
