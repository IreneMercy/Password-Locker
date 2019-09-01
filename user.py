import getpass
class User:
    '''
    A class that promts user to signup and login to generate passwords
    '''
    def __init__(self,username, email, password):
        '''
        method that defines the properties of each user
        '''
        self.username = username
        self.email = email
        self.password = password
    user_list = []
    def save_Users(self):
        User.user_list.append(self)
