from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from TwoMarch.Utilities import MyUtilities

class LoginPageFlows():

    driverInst = None

    def __init__(self):
        LoginPageFlows.driverInst = MyUtilities.Mydriver()


    def LoginInToAccount(self,Uname,Password):
        LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="txtUsername"]').send_keys(Uname)
        LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(Password)
        LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="btnLogin"]').click()

    def GetErrorText(self):
        try:
            return LoginPageFlows.driverInst.find_element_by_id('spanMessage').text
        except:
            None

