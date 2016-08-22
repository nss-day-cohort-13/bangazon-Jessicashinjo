from user import *
from chirps import *
from private_chirps import *
from conversation import *
from service_functions import *

class Birdyboard():
  def __init__(self):
    """ Keeps track of the active user and that user's screen name

    Arguments:
    ----------
    """
    self.active_user = None
    self.active_screen_name = None

  def welcome_menu(self):
    """
    Main selection Menu for the birdyboard application. From here the user can
    choose to create a new account, select a current user, view all chirps,
    create a new public chirp, create a new private chirp, or exit the app.


    Arguments:
    ----------
    """
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
      self.create_new_user()
    if choice == '2':
      active_user = self.select_user()
      self.active_user = active_user.user_id
      self.active_screen_name = active_user.screen_name
      self.view_chirps()
    if choice == '3':
      self.view_chirps()
    if choice == '4':
      self.create_public_chirp()
    if choice == '5':
      self.create_private_chirp()
    if choice == '6':
      exit()

  def create_new_user(self):
    """ Takes input of the users full name and screen name to create a new user

    Arguments:
    ----------
    """
    user_full_name = input("Enter your name > ")
    user_screen_name = input("Create a screen name > ")
    new_user = User(user_full_name, user_screen_name)
    self.active_user = new_user.user_id
    self.active_screen_name = new_user.screen_name

    self.welcome_menu()

  def select_user(self):
    """
    Prints a list of screen names to choose from. The user can then select their
    screen name to see of his or her chirps.

    Arguments:
    ----------
    """
    user_list = deserialize("user_data.txt")
    counter = 3
    print("1. Main Menu")
    print("2. Exit")
    for user in user_list:
      print(str(counter) + ". " + str(user.screen_name))
      counter += 1

    choice = int(input("Select a user > "))
    if choice == 1:
      Birdyboard.welcome_menu()
    if choice == 2:
      exit()
    else:
      return user_list[(choice - 3)]

      # print(Birdyboard.active_user)
      # new_conversation = Conversation(user_list[(choice - 3)]["user_UUID"], user_list[(choice - 3)]["chirp_UUID"], 0)
      # Birdyboard.active_order = new_order.order_UUID
      # print("Welcome " + )

  def view_chirps(self):
    """
    Displays a list of numbered chirps which are separated by public and private.
    The user is only able to see the public chirps and chirps which he or she
    has sent or received privately.

    Arguments:
    ----------
    """
    counter = 3
    print(
          '\n'
          "~~~~~Public Chirps~~~~~"'\n'
          )
    public_chirp_list = deserialize("chirps.txt")
    # public_chirp_list.sort(key=lambda x: x["timestamp"])
    temp_public_chirp_dict = {}
    print("1. Main Menu")
    print("2. Exit")
    for chirp in public_chirp_list:
      print(str(counter) + ". " + str(chirp.screen_name) + ": " + str(chirp.message))
      temp_public_chirp_dict[counter] = chirp
      # print(chirp)
      counter += 1

    print(
          '\n'
          "~~~~~Private Chirps~~~~~"'\n'
          )
    private_chirp_list = deserialize("private_chirps.txt")
    # private_chirp_list.sort(key=lambda x: x["timestamp"])
    temp_private_chirp_dict = {}
    if self.active_user != None:
      # user_list = deserialize("user_data.txt")
      for chirp in private_chirp_list:
        if self.active_user == chirp.user_uuid:
          print(str(counter) + ". To: " + str(chirp.receiver_screen_name) + "- " + str(chirp.message))
          temp_private_chirp_dict[counter] = chirp
          # print("Temp dict", temp_private_chirp_dict)
          counter += 1
        if self.active_user == chirp.receiver_id:
          print(str(counter) + ". From: " + str(chirp.screen_name) + "- " + str(chirp.message))
          temp_private_chirp_dict[counter] = chirp
          counter += 1

    else:
      print(
            "You don't have any private chirps."
            )
    # print(public_chirp_list)
    # print(private_chirp_list)
    # print("this user is active", self.active_user)

    # THIS SECTION CAN BE EXAPANDED INTO CONVERSATIONS/THREADS
    conversation_list = deserialize("conversations.txt")
    choice = int(input("Where to? > "))
    if choice == 1:
      self.welcome_menu()
    if choice == 2:
      exit()
    else:
      print("Please select choice 1 or 2")
      self.view_chirps()
      # print(temp_public_chirp_dict)
      # for public_counter, chirp in temp_public_chirp_dict.items():
      #   # print("public counter", public_counter)
      #   if choice == public_counter:
      #     for conversation in conversation_list:
      #       if chirp.chirp_id == conversation.chirp_UUID:
      #         self.view_thread(conversation.conversation_UUID)
      # for private_counter, chirp in temp_private_chirp_dict.items():
      #   if choice == private_counter:
      #     for conversation in conversation_list:
      #       if chirp.chirp_id == conversation.chirp_UUID:
      #         self.view_thread(conversation.conversation_UUID)
      #
      #   customer_list[(choice - 3)].customer_UUID
      #
      #   new_order = Order(customer_list[(choice - 3)].customer_UUID, 0)
      #   Crime.active_order = new_order.order_UUID

  # def view_thread(self, conversation_id):
  #   print("Yo convo ID", conversation_id)
  #   pass

  def create_public_chirp(self):
    """ Uses the active user's input to create a public chirp

    Arguments:
    ----------
    """
    if self.active_user != None:
      message = input("What do you want to say? > ")
      new_chirp = Chirps(self.active_user, self.active_screen_name, message)
      Conversations(new_chirp.user_uuid, new_chirp.chirp_id, None)
      self.view_chirps()
    else:
      print(
            '\n'
            "Please sign in or create an account to post."'\n'
            "1. Return to Welcome Screen"'\n'
            "2. Exit program"'\n'
            )
      choice = int(input("What would you like to do? > "))
      if choice == 1:
        self.welcome_menu()
      if choice == 2:
        exit()

  def create_private_chirp(self):
    """ Uses the active user's input to create a private chirp.

    Arguments:
    ----------
    """
    if self.active_user != None:
      receiver = self.select_user()
      receiver_id = receiver.user_id
      receiver_screen_name = receiver.screen_name

      message = input("What do you want to say? > ")
      new_chirp = PrivateChirps(self.active_user, self.active_screen_name, message, receiver_id, receiver_screen_name)
      Conversations(new_chirp.user_uuid, new_chirp.chirp_id, receiver_id)
      self.view_chirps()
    else:
      print(
            '\n'
            "Please sign in or create an account to post."'\n'
            "1. Return to Welcome Screen"'\n'
            "2. Exit program"'\n'
            )
      choice = int(input("What would you like to do? > "))
      if choice == 1:
        self.welcome_menu()
      if choice == 2:
        exit()



if __name__ == '__main__':
  Birdyboard().welcome_menu()
  # birdy = Birdyboard()
  # birdy.create_user("Joe", "Joeisnaihs")
  # birdy.read_users()
  # birdy.read_chirps("Jessicasa")
  # birdy.write_chirp("Jess", "Jessicasa", True, "Public", "Chirpy Chirpy man")

# Separate functions to see if user_exists and screen_name exists?
