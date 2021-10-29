import random
import string

from selenium import webdriver

class addCustomer:
    link_customer_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_submenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_addnew_xpath="//a[normalize-space()='Add new']"
    text_email_xpath="//input[@id='Email']"
    text_password_xpath="//input[@id='Password']"
    text_firstname_xpath="//input[@id='FirstName']"
    text_lastname_xpath="//input[@id='LastName']"
    radio_male_id = "Gender_Male"
    radio_female_id = "Gender_Female"
    dob_id = "DateOfBirth"
    text_company_xpath="//input[@id='Company']"
    check_istaxexempt_xpath = "//input[@id='IsTaxExempt']"
    dd_newlatter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    list_customerorles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    dd_managervendor_xpath = "//select[@id='VendorId']"
    txt_admincomment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']//i[@class='far fa-save']"

    def __init__(self,driver):
        self.driver=driver

    def clickcustomer(self):
        self.driver.find_element_by_xpath(self.link_customer_menu_xpath).click()
    def clicksubcustomer(self):
        self.driver.find_element_by_xpath(self.link_customer_submenu_xpath).click()
    def clickaddnew(self):
        self.driver.find_element_by_xpath(self.link_addnew_xpath).click()

    def setemail(self, Email):
        self.driver.find_element_by_xpath(self.text_email_xpath).send_keys(Email)
    def setpassword(self, password):
        self.driver.find_element_by_xpath(self.text_password_xpath).send_keys(password)
    def setfirstname(self, firstname):
        self.driver.find_element_by_xpath(self.text_firstname_xpath).send_keys(firstname)
    def setlastname(self, lastname):
        self.driver.find_element_by_xpath(self.text_lastname_xpath).send_keys(lastname)
    def setcampany(self, campany):
        self.driver.find_element_by_xpath(self.text_company_xpath).send_keys(campany)
    def setadmincomment(self, admincomment):
        self.driver.find_element_by_xpath(self.txt_admincomment_xpath).send_keys(admincomment)

def random_generator(size=8, chars=string.ascii_letters+string.digits):
    return ''.join(random.choice(chars) for x in range(size))