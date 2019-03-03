import unittest
from TwoMarch.LoginPage import LoginPageFlows

class MyTestCaseDemo(unittest.TestCase):

    @unittest.skip('GM Condition test')
    def test_Login_Valid(self):
        LoginPageObj = LoginPageFlows()
        LoginPageObj.LoginInToAccount('Admin','admin123')

    def test_Login_UserNameTest(self):
        LoginPageObj = LoginPageFlows()
        LoginPageObj.LoginInToAccount('','admin123')
        MyMsg = LoginPageObj.GetErrorText()
        self.assertEqual('Username cannot be empty',MyMsg)

    def test_Login_PasswordTest(self):
        LoginPageObj = LoginPageFlows()
        LoginPageObj.LoginInToAccount('Admin','')
        MyMsg = LoginPageObj.GetErrorText()
        self.assertEqual('Password cannot be empty',MyMsg)

    def test_Login_Invalid(self):
        LoginPageObj = LoginPageFlows()
        LoginPageObj.LoginInToAccount('Admin','admin1234')
        MyMsg = LoginPageObj.GetErrorText()
        self.assertEqual('Invalid credentials',MyMsg)

if __name__ == '__main__':

    unittest.main()
