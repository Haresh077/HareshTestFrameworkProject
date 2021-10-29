import time

from pageObjects.LoginPage import Login
from pageObjects.AddCustomer import addCustomer, random_generator
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
import pytest


class Test_001_addCustomer:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("**************Add Customer***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("*******Login successfull*********")
        self.addcust = addCustomer(self.driver)
        time.sleep(5)
        self.addcust.clickcustomer()
        self.addcust.clicksubcustomer()
        self.addcust.clickaddnew()
        self.email= random_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        self.addcust.setpassword("test123")
        self.addcust.setfirstname("haresh")
        self.addcust.setlastname("Sankaliya")
        self.addcust.setcampany("Haresh Test")
        self.addcust.setadmincomment("Test comment")
        time.sleep(10)
        self.driver.close()


