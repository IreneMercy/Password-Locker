#!/usr/bin/env python3.7
from credentials_locker import Credentials, User
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

def save_user(User):
    '''
    function to save user
    '''
    User.save_user()

def delete_credential(Credentials):
    '''
    a function to delete credential
    '''
    Credentials.delete_credential()
def check_existing_credentials(username):
    '''
    functions that checks if a credential exist using app_name
    '''
    return Credentials.find_by_username(username)

def find_credential(username):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.find_by_username(username)
def display_credentials():
    '''
    function that displays all the credentials
    '''
    return Credentials.display_credentials()
def generate_password(length):
    '''
    function that generates passwords
    '''
    return Credentials.passwordGenarator(5)

def main():
    print("Hello, Welcome to Password Locker")
    print("Enter your user details to signup:")
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
    save_user(create_user(username,email,password)) #Creates and saves user
    print("\n")
    print(f"New User {username} {email} {password} has been created")
    print("\n")

    while True:
        print("Use these short codes : NC - create a new credential, DC - display credential, FC -find a credential, EX -exit the password locker ")
        short_code = input().upper()

        if short_code == "EX":
            break

        elif short_code == "DC":
            if(display_credentials):
                print("Here is a list of your credentials")
                print("\n")
                for credential in display_credentials():
                    print(f"{credential.app_name} {credential.username} .....{credential.password}")
                    print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any credentials saved yet")
                    print('\n')

        elif short_code == 'FC':
            print("Enter the username you want to search for")
            search_app = input()
            if check_existing_credentials(username):
                search_credential = find_credential(search_app)
                print(f"{search_credential.username}")
                print('-' * 20)
                print(f"App name.......{search_credential.app_name}")
                print(f"Username.......{search_credential.username}")
                print(f"Password.......{search_credential.password}")

            else:
                    print("That contact does not exist")
        if short_code == "NC":
            print("New credential")
            print("Enter app_name")
            app_name = input()
            print("Enter username")
            username = input()
            print("Your generated password is:")
            gnpass = Credentials.passwordGenarator(5)
            print(gnpass)
            print("Or use your choice password")
            password = input()
            save_credentials(create_credential(app_name,username,password)) #Creates and saves user
            print("\n")
            print(f"New Credential {app_name} {username} {password} has been created")
            print("Credential saved succesfully")


if __name__ == '__main__':
    main()
