
class Birdyboard():

  def create_user(self, full_name, screen_name):
    ''' Takes arguements of the users full name and the user's screen name:

    Checks to see if user_data file exists. If the file does not exist
    it will create the file and add the user. If it does exist, it will read
    the user_data file to see if user exists. If the user exists there will
    be an error thrown. If the user does not exist, it will generate a user_id
    and he or she will be added to the csv file with the user_id, full_name,
    and screen_name.
    '''
    pass

  def write_chirp(self, full_name, privacy, to_whom, message):
    ''' Takes arguments of the users full name, if it should be public or
        private, who the chirp will be sent to, and the message itself:

    Opens user_data and searches for user. If the file does not contain user,
    throws an error to sign up and sends user back to the menu. If it does
    contain user it will close the file and open the chirps file. Next it will
    check the privacy. If privacy is public it will generate a chirp_id
    and write the chirp_id, full_name, privacy, to_whom (automatically listed
    as "public" if privacy is public), and message to the chirps.csv file.
    '''
    pass

  def read_chirps(self, full_name):

    pass

  def delete_chirp():
    pass
