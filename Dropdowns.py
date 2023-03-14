import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# service_obj= Service("C:\\Sandeep_Python\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome(executable_path='C:\\Sandeep_Python\\chromedriver_win32\\chromedriver.exe')


driver.get("https://www.facebook.com/")

driver.find_element(By.XPATH,"//div/a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
time.sleep(3)

Day = driver.find_element(By.XPATH,"//select[@id='day']")
time.sleep(3)
Birthday = Select(Day)
Birthday.select_by_index(21)
time.sleep(3)
Birthday.select_by_visible_text("30")
time.sleep(3)
Birthday.select_by_visible_text("31")
time.sleep(5)