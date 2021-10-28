from selenium import webdriver
class addCustomer:
    link_customer_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
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

    def setusername(self, Email):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(Email)
