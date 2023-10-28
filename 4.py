from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time 
  

driver = webdriver.Chrome() 
driver.get("https://www.facebook.com/login/") 

  

expected_title = "Log in to Facebook" 
actual_title = driver.title

if expected_title == actual_title: 
    print("Verification Successful - The correct title is displayed on the web page.") 
else: 
    print("Verification Failed - An incorrect title is displayed on the web page.") 

username = driver.find_element(By.ID, "email") 

username.clear() 

username.send_keys("") 

password = driver.find_element(By.ID, "pass") 

password.clear() 

password.send_keys("") 

password.send_keys(Keys.ENTER) 
time.sleep(10)
driver.close() 

print("Test script executed successfully.") 