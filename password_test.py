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

    def test_save_credentials(self):
        '''
        tests if the credential object is saved
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def tearDown(self):
        '''
        clean up after each test case has been run
        '''
        Credentials.credential_list = []

    def test_save_multiple(self):
        '''
        tests if we can save multiple credentials to the credentials list
        '''
        self.new_credentials.save_credentials()
        whatsap_credential = Credentials("Irene","Mercy","irenemercy700@gmail.com","joozao700","IreneMercy")
        whatsap_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)




if __name__ == '__main__':
    unittest.main()
