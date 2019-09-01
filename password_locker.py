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
        save creentials into the credential_list
        '''
        Credentials.credential_list.append(self)
