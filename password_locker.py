import getpass
import string, random
class User:
    '''
    A class that promts user to signup and login to generate passwords
    '''
    print("Welcome, create an account to login")
    print("Enter Username")
    username = input()
    print("Enter Email")
    email = input()
    print("Enter Password")
    password = getpass.getpass()
    print("Confirm  password to login")

    Confirmpassword = getpass.getpass()

    if password == Confirmpassword:
        print("Welcome to Password generator")
    False

    # def passwordGenarator(length):
    #     print("Your generated  password is:")
    #     password = ''
    #     for i in range(length):
    #         n = random.randint(0,20)
    #         password += string.printable[n]
    #     return password
    # print (passwordGenarator(5))


class Credentials:
    '''
    Class that generates ne password credentials
    '''
    credential_list = []
    def __init__(self, password, username):
        '''
        __init__ metho that generate properties for our objects
        '''
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
        for credentials in cls.credential_list:
            '''
            a for loop to loop through the list and check if the credential exists
            '''
            if credentials.username == username:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        '''
        method that displays all the credentials in the credential_list
        '''
        return cls.credential_list
