import unittest
# **importing unittest module**
from password_locker import Credentials
# **importing class password **
class testPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the password behaviour
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases
        unittest.testcase helps in creating tests
        '''
        self.new_credentials= Credentials("Irene","Mercy","irenemercy700@gmail.com","@joozao","joozao")
    def test_init(self):
        '''
        Test if the object is initialized correctly
        '''
        self.assertEqual(self.new_credentials.first_name,"Irene")
        self.assertEqual(self.new_credentials.last_name,"Mercy")
        self.assertEqual(self.new_credentials.email,"irenemercy700@gmail.com")
        self.assertEqual(self.new_credentials.password,"@joozao")
        self.assertEqual(self.new_credentials.username,"joozao")
if __name__ == '__main__':
    unittest.main()
