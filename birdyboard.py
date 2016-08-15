from user import *
from chirps import *
from private_chirps import *
from conversation import *
from service_functions import *

class Birdyboard():
  def __init__(self):
    self.active_user = ""

  @staticmethod
  def welcome_menu():
    print(
          '\n'
          "#########################################"'\n'
          "##       ~~~~~ Birdyboard ~~~~~        ##"'\n'
          "#########################################"'\n'
          '\n'
          "1. New User Account"'\n'
          "2. Select User"'\n'
          "3. View Chirps"'\n'
          "4. Public Chirp"'\n'
          "5. Private Chirp"'\n'
          "6. Exit"'\n'
          '\n''\n'
          )

    choice = input("> ")
    if choice == '1':
      Birdyboard.create_new_user()
    if choice == '2':
      Birdyboard.select_user()
    if choice == '3':
      Birdyboard.view_chirps()
    if choice == '4':
      Birdyboard.create_public_chirp()
    if choice == '5':
      Birdyboard.create_private_chirp()
    if choice == '6':
      exit()

  def create_new_user():

    user_full_name = input("Enter your name > ")
    user_screen_name = input("Create a screen name > ")
    new_user = User(user_full_name, user_screen_name)
    Birdyboard.active_user = new_user.user_id

  def select_user():
    deserialize("user_data.txt")

  def view_chirps():
    pass

  def create_public_chirp():
    pass

  def create_private_chirp():
    pass



if __name__ == '__main__':
  Birdyboard.welcome_menu()
  # birdy = Birdyboard()
  # birdy.create_user("Joe", "Joeisnaihs")
  # birdy.read_users()
  # birdy.read_chirps("Jessicasa")
  # birdy.write_chirp("Jess", "Jessicasa", True, "Public", "Chirpy Chirpy man")

# Separate functions to see if user_exists and screen_name exists?
