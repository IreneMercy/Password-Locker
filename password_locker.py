class Credentials:
    '''
    Class that generates ne password credentials
    '''
    credential_list = []
    def __init__(self, first_name, last_name, email, password, username):
        '''
        __init__ metho that generate properties for our objects
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
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
            if credential.username == username:
                return credential
        for credentials in cls.credential_list:
            if credentials.username == username:
                return True
        return False
