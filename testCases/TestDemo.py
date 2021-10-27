from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

s=Service("D:\\Haresh\\PythonQA\\HareshTestFrameworkProject\\Drivers\\chromedriver950.exe")

driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/")

time.sleep(5)

driver.close()