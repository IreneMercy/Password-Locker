#!/usr/bin/env python3.7
from credentials_locker import Credentials
import getpass
import random, string
from user import User


def create_credential(username, password):
    '''
    Function to create a new contact
    '''
    new_credential = Credentials(username, password)
    return new_credential

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
    print("Welcome, You can add and create new credentials")
    print("Enter Username")
    username = input()
    password = ''
    for i in range(length):
        n = random.randint(0,20)
        password += string.printable[n]
    print("Your generated password is:")
    print(password)
    print("Enter your own Password? or generated one?")
    password = getpass.getpass()
    print("Confirm  password to save your credentials")
    Confirmpassword = getpass.getpass()
    if password == Confirmpassword:
        print("Thanks for using Password Locker")
    False
(passwordGenarator(5))

if __name__ == '__main__':
    main()
