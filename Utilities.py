from selenium import webdriver


class MyUtilities:

    @staticmethod
    def Mydriver(browser = "Chrome"):

        if browser == "Chrome":
            driver = webdriver.Chrome('E:\\Ganesh\\Drivers\\chromedriver.exe')
        else :
            pass
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        return driver