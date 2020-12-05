from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("sample test case started")
driver = webdriver.Chrome(r"C:\Users\anjalip\myProjects\selenium-2.53.1\Demo\browser\chromedriver.exe")
# driver=webdriver.firefox()
# driver=webdriver.ie()
# maximize the window size
driver.maximize_window()
# navigate to the url
driver.get("https://mywallst.com/")
time.sleep(3)
# identify the Google search text box and enter the value
driver.find_element_by_xpath("/html/body/header/div/div/div/div/nav/ul/li[6]/a/span").click()
time.sleep(3)
# click on the Google search button



driver.find_element_by_name("username").send_keys('anjali.parmar@somaiya.edu')
time.sleep(3)
driver.find_element_by_name("password").send_keys('Anjali@123')
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/main/section/div/div[2]/form/p[3]/button/span").click()

time.sleep(3)


# close the browser
driver.close()
print("sample test case successfully completed")
