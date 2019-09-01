class Credentials:
    '''
    Class that generates ne password credentials
    '''
    def __init__(self, first_name, last_name, email, password, username):
        '''
        __init__ metho that generate properties for our objects
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.username = username
