from pageObjects.LoginPage import Login
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
import pytest


class Test_001_login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()

    def test_homepagetitle(self, setup):
        self.logger.info("**************Test_001_login***********")
        self.logger.info("**************Verify homepage title***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************Homepage title test is passed***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**************Homepage title test is failed***********")
            assert False

    def test_login(self, setup):
        self.logger.info("**************Verify login test***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************Login test is passed***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("**************login test is failed***********")
            assert False
