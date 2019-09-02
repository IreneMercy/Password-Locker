import getpass
import random, string

class User():
    '''
    A class that promts user to signup and login to generate passwords
    '''
    user_list = []
    def __init__(self,username,email,password):
        '''
        a method to define user proprties
        '''
        self.username = username
        self.email = email
        self.password = password
    def save_user(self):
        '''
        a method that saves user
        '''
        User.user_list.append(self)

class Credentials:
    '''
    Class that generates ne password credentials
    '''
    credential_list = []
    def __init__(self,app_name, password, username):

        '''
        __init__ method that generate properties for our objects
        '''
        self.app_name = app_name
        self.password = password
        self.username = username

    def save_credentials(self):
        '''
        method that saves a credential
        enables user to save creentials into the credential_list
        '''
        Credentials.credential_list.append(self)


    def delete_credential(self):
        '''
        method that deletes a credential
        enable user to delete credential
        '''
        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        method that takes a username and return credential that matches it
        enable user to search for a specific credential
        '''
        for credential in cls.credential_list:
            '''
            a for loop to loop through the list and return the credential that matches the username
            '''
            if credential.username == username:
                return credential
        for user in User.user_list:
            '''
            a for loop to loop through the list and check if the credential exists
            '''
            if user.username == username:
                present_user = user.username
                return present_user
        return "User does not exist"

    @classmethod
    def display_credentials(cls):
        '''
        method that displays all the credentials in the credential_list
        '''
        return cls.credential_list

    def passwordGenarator(length):
        '''
        a method that generates passwords for the user
        '''
        for i in range(length):
            password = ''
            n = random.randint(0,20)
            password += string.printable[n]

    (passwordGenarator(5))
