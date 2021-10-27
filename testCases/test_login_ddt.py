import time

from pageObjects.LoginPage import Login
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities import XLutilities


class Test_002_DDT_login:
    baseURL = Readconfig.getApplicationURL()
    logger = LogGen.loggen()
    path="D:\\Haresh\\PythonQA\\HareshTestFrameworkProject\\TestData\\Logindetails.xlsx"

    def test_login(self, setup):
        self.logger.info("**************Test_002_DDT_login***********")
        self.logger.info("**************Verify login DDT test***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.rows=XLutilities.getRowCount(self.path, 'Sheet1')
        print("Number of rows", self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=XLutilities.readdata(self.path,'Sheet1', r, 1)
            self.password = XLutilities.readdata(self.path, 'Sheet1',r, 2)
            self.exp= XLutilities.readdata(self.path, 'Sheet1', r, 3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            self.lp.clicklogout()
            time.sleep(3)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Pass")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*****failed")
                    self.lp.clicklogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Failed")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*****Passed")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("***Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("***************Login DDT test failed")
            self.driver.close()
            assert False
        self.logger.info("*******End of login DDT test")
        self.logger.info("*******Completed TC_loginDDT_002")