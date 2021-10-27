from selenium import webdriver

class Login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    btn_login_xpath="//button[normalize-space()='Log in']"
    btn_logout_xpath = "// a[contains(text(), 'Logout')]"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_xpath(self.btn_logout_xpath).click()


