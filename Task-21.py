from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set path to ChromeDriver executable
serv_obj=Service(r"C:\Drivers_Selenium\chromedriver-win64\chromedriver.exe")

# Create new instance of Chrome driver
driver = webdriver.Chrome(service=serv_obj)

# Maximize browser window
driver.maximize_window()

# Open URL
driver.get('https://www.saucedemo.com/')

# Display cookies before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:", cookies_before_login)

# Find username, password, and login button elements
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

#time delay
time.sleep(3)

# Display cookies after login
cookies_after_login = driver.get_cookies()
print("Cookies after login:", cookies_after_login)

#time delay
time.sleep(3)

# Clicking on inventory item
driver.find_element(By.ID,"react-burger-menu-btn").click()

time.sleep(4)

# Logout
driver.find_element(By.ID,"logout_sidebar_link").click()

# Display cookies after logout
cookies_after_logout = driver.get_cookies()
print("Cookies after logout:", cookies_after_logout)

#time delay
time.sleep(4)

# Close browser
driver.close()