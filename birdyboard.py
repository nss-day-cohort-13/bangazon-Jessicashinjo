import csv

class Birdyboard():

  def create_user(self, full_name, screen_name):
    ''' Takes arguments of the user's full name and the user's screen name:

    Checks to see if user_data file exists. If the file does not exist
    it will create the file and add the user. If it does exist, it will read
    the user_data file to see if user exists. If the user exists there will
    be an error thrown. If the user does not exist, it will generate a user_id
    and he or she will be added to the csv file with the user_id, full_name,
    and screen_name.
    '''

    with open("user_data.csv", "a+") as f:
      user_data = full_name, screen_name
      writer = csv.writer(f, delimiter=',')
      writer.writerow(user_data)

    # try:
    # except Exception as e:
    #   raise

  def read_users(self):
    user_data = list()
    with open("user_data.csv", "r+") as f:
      reader = csv.reader(f)
      for row in reader:
        user_data.extend(row)

    return user_data

  def write_chirp(self, full_name, screen_name, privacy, to_whom, message):
    ''' Takes arguments of the user's full name, screen name, if it should be
        public or private, who the chirp will be sent to, and the message
        itself:

    Opens user_data and searches for user. If the file does not contain user,
    throws an error to sign up and sends user back to the menu. If it does
    contain user it will close the file and open the chirps file. Next it will
    check the privacy. If privacy is public it will generate a chirp_id
    and write the chirp_id, full_name, screen_name, privacy, to_whom
    (automatically listed as "public" if privacy is public), and message to the
    chirps.csv file.
    '''
    pass

  def read_chirps(self, screen_name):
    ''' Takes the user's screen_name as its argument:

    Opens user_data.csv file and searches for the screen_name. If the
    screen_name does not exist it will only print public chirps. If the
    screen_name does exist it will print public and the user's private chirps in
    separate sections.
    '''
    pass

  def delete_chirp(self, screen_name, chirp_id):
    ''' Takes arguments of the user's screen name and id of the message to be
        deleted:

    First it will open the user_data.csv and check to see if the owner of the
    chirp is the one deleting chirp. If the person deleting the chirp is not
    the owner, it will throw an error saying "You cannot delete another user's
    chirp". If the person deleting the chirp is the owner, it will remove the
    chirp (without asking "Are you sure?") and allow the user to continue to
    delete chirps until they are done.
    '''
    pass

if __name__ == '__main__':
  birdy = Birdyboard()
  birdy.create_user("Jess", "Jessicasa")
  birdy.read_users()

# Separate functions to see if user_exists and screen_name exists?
