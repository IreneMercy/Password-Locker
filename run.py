#!/usr/bin/env python3.7
from credentials_locker import Credentials
import getpass
def create_credential(app_name,username, password):
    '''
    function to create a new credential
    '''
    new_credential = Credentials(app_name,username,password)
    return new_credential

def create_user(username,email,password):
    '''
    function to create a new user
    '''
    new_user = User(username,email,password)
    return new_user

def save_credentials(Credentials):
    '''
    function to save credentials
    '''
    Credentials.save_credentials()

def save_credentials(User):
    '''
    function to save user
    '''
    User.save_user()

def delete_credential(Credentials):
    '''
    a function to delete credential
    '''
    Credentials.delete_credential()
def check_existing_credentials(app_name):
    '''
    functions that checks if a credential exist using app_name
    '''
    return Credentials.find_by_username()
def display_credentials():
    '''
    function that displays all the credentials
    '''
    return CredentialS.display_credentials()
def generate_password():
    '''
    function that generates passwords
    '''
    return Credentials.passwordGenarator()

def main():
    print("Hello, Welcome to Password Locker")
    print("Enter your user details to login:")
    print("\n")
    print("Enter Username")
    username = input()
    print("Enter email")
    email = input()
    print("Enter Password")
    password = getpass.getpass()
    print("Confirm password to login")
    confirmPassword = getpass.getpass()
    if confirmPassword == password:
        print("\n")
        print("Welcome to Password Locker")
    False

    while True:
        print("Use these short codes : NC - create a new credential, DC - display credential, FC -find a credential, EX() -exit the password locker ")
        short_code = input().upper()
        if short_code == "NC":
            print("New credential")
            print("Enter app_name")
            app_name = input()
            print("Enter username")
            username = input()
            print("Your generated password is:")
            password = generate_password()
            print(password)

if __name__ == '__main__':
    main()
