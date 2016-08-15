from user import *
from chirps import *
from private_chirps import *
from conversation import *
from service_functions import *

class Birdyboard():
  def __init__(self):
    self.active_user = ""

  def welcome_menu(self):
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
      self.view_chirps()
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
    self.active_user = new_user.user_id

  def select_user():
    user_list = deserialize("user_data.txt")
    counter = 3
    print("1. Main Menu")
    print("2. Exit")
    for user in user_list:
      print(str(counter) + ". " + str(user["user_screen_name"]))
      counter += 1

    choice = int(input("Select your user_name > "))
    if choice == 1:
      Birdyboard.welcome_menu()
    if choice == 2:
      exit()
    else:
      self.active_user = user_list[(choice - 3)]["user_uuid"]
      # print(Birdyboard.active_user)
      # new_conversation = Conversation(user_list[(choice - 3)]["user_UUID"], user_list[(choice - 3)]["chirp_UUID"], 0)
      # Birdyboard.active_order = new_order.order_UUID
      # print("Welcome " + )
      self.view_chirps()

  def view_chirps(self):
    print(
          '\n'
          "~~~~~Public Chirps~~~~~"'\n'
          )
    public_chirp_list = deserialize("chirps.txt")
    public_chirp_list.sort(key=lambda x: x["timestamp"])
    counter = 3
    print("1. Main Menu")
    print("2. Exit")
    for chirp in public_chirp_list:
      print(str(counter) + ". " + str(chirp["user_screen_name"]) + ": " + str(chirp["message"]) + str(chirp["timestamp"]))
      counter += 1

    print(
          '\n'
          "~~~~~Private Chirps~~~~~"'\n'
          )
    if self.active_user != "":
      private_chirp_list = deserialize("private_chirps.txt")
      private_chirp_list.sort(key=lambda x: x["timestamp"])
      # user_list = deserialize("user_data.txt")
      print("1. Main Menu")
      print("2. Exit")
      for chirp in private_chirp_list:
        if self.active_user == chirp["user_uuid"]:
          print(str(counter) + ". " + str(chirp["receiver_screen_name"]) + ": " + str(chirp["message"]) + str(chirp["timestamp"]))
          counter += 1
        if self.active_user == chirp["receiver_id"]:
          print(str(counter) + ". " + str(chirp["user_screen_name"]) + ": " + str(chirp["message"]) + str(chirp["timestamp"]))
          counter += 1
        # for user in user_list:
          # if chirp[]:
    else:
      print(
            "You don't have any private chirps."
            )

  def create_public_chirp():
    pass

  def create_private_chirp():
    pass



if __name__ == '__main__':
  Birdyboard().welcome_menu()
  # birdy = Birdyboard()
  # birdy.create_user("Joe", "Joeisnaihs")
  # birdy.read_users()
  # birdy.read_chirps("Jessicasa")
  # birdy.write_chirp("Jess", "Jessicasa", True, "Public", "Chirpy Chirpy man")

# Separate functions to see if user_exists and screen_name exists?
