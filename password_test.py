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
        method that tests if the object is initialized correctly
        '''
        self.assertEqual(self.new_credentials.first_name,"Irene")
        self.assertEqual(self.new_credentials.last_name,"Mercy")
        self.assertEqual(self.new_credentials.email,"irenemercy700@gmail.com")
        self.assertEqual(self.new_credentials.password,"@joozao")
        self.assertEqual(self.new_credentials.username,"joozao")

    def test_save_credentials(self):
        '''
        method that tests if the credential object is saved
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def tearDown(self):
        '''
        method that cleans up after each test case has been run
        '''
        Credentials.credential_list = []

    def test_save_multiple(self):
        '''
        method that tests if we can save multiple credentials to the credentials list
        '''
        self.new_credentials.save_credentials()
        whatsap_credential = Credentials("Irene","Mercy","irenemercy700@gmail.com","joozao700","IreneMercy")
        whatsap_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_credential(self):
        '''
        method that tests if we can delete a credential
        '''
        self.new_credentials.save_credentials()
        whatsap_credential = Credentials("Irene","Mercy","irenemercy700@gmail.com","joozao700","IreneMercy")
        whatsap_credential.save_credentials()
        self.new_credentials.delete_credential()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_find_credential_by_username(self):
        '''
        method that tests if the credential is available and can be found by searching username
        '''
        self.new_credentials.save_credentials()
        whatsap_credential = Credentials("Irene","Mercy","irenemercy700@gmail.com","joozao700","IreneMercy")
        whatsap_credential.save_credentials()
        credentials_found = Credentials.find_by_username("IreneMercy")
        self.assertEqual(credentials_found.username,whatsap_credential.username)


    def test_check_credentials_exists(self):
        '''
        method that tests to check if the creential exists
        '''
        self.new_credentials.save_credentials()
        whatsap_credential = Credentials("Irene","Mercy","irenemercy700@gmail.com","joozao700","IreneMercy")
        whatsap_credential.save_credentials()
        credential_exits = Credentials.find_by_username("IreneMercy")
        self.assertTrue(credential_exits)

    def test_display_all_credentials(self):
        '''
        method that tests if we can return all the credential in credential_list
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)



if __name__ == '__main__':
    unittest.main()
