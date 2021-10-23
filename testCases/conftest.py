from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="D:\\Python\\chromedriver_win32\\chromedriver_94.0.exe")
        driver.maximize_window()
    elif browser=='firefox':
        driver=webdriver.firefox()
    elif browser=='IE':
        driver=webdriver.ie
    else:
        drive=webdriver.chrome(executable_path="D:\\Python\\chromedriver_win32\\chromedriver_94.0.exe")
    return driver

def pytest_addoption(parser):  #This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This will return the browser value to setup method
    return request.config.getoption("--browser")

################## Pytest HTML Report ##################
#it is hook for adding Environment info for HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] ='nop commerce'
    config._metadata['Module Name'] ='Customer'
    config._metadata['Tester'] ='Haresh'

# it is hook for delete/modify Environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)