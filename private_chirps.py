from chirps import *
from service_functions import *

class PrivateChirps(Chirps):
  def __init__(self, user_id, user_screen_name, message, receiver_id, receiver_screen_name):
    """ Inherits from Chirps to produce private chirp

    Arguments:
    ----------
    user_id(int) = id of user creating the chirp
    user_screen_name(str) = screen name of the user creating the chirp
    message(str) = content of the user's message
    receiver_id(int) = id of the chirp recipient
    receiver_screen_name(str) = screen name of the chirp recipient
    """
    self.receiver_id = receiver_id
    self.receiver_screen_name = receiver_screen_name
    super().__init__(user_id, user_screen_name, message, "private_chirps.txt", False)



# if __name__ == '__main__':
  # PrivateChirps(86419575609614075990463230600833442718, 'check_yoself', "Do private chirps work?", 148483404200007806254540872871643687611, 'test_yoself')
  # chirps.create_public_chirp('JJPop', "Public service announcement yoooo")
  # result = deserialize("private_chirps.txt")
  # for item in result:
  #     print(item.__dict__)
