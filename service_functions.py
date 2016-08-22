import pickle
import uuid
from datetime import datetime
from time import time

def serialize(file_name, object):
  """ Pickles the object provided

  Arguments:
  file_name(str) = Name of the file storing the serialized deserialized_data
  object(*) = Can accept any type of information including list, dict, etc
  """
  with open(file_name, "ab+") as pickle_file:
    pickle.dump(object, pickle_file)

def deserialize(file_name):
  """ Depickles all information from the file provided and returns the
      information as a list

  Arguments:
  file_name(str) = Name of the file storing the serialized deserialized_data
  """
  with open(file_name, "rb") as pickle_file:
    deserialized_data = []
    while True:
      try:
        deserialized_data.append(pickle.load(pickle_file))
      except FileNotFoundError:
        print("i'm a duck")
      except EOFError:
        break

    # print(deserialized_data)
    return deserialized_data

def timestamp():
  """ Creates new timestamp at the current time """
  current_time = time()
  time_stamp = datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')
  return time_stamp

def generate_uuid():
  """ Generates a random interger ID """
  return uuid.uuid4().int
