from selenium import webdriver 

from selenium.webdriver.common.by import By 

driver = webdriver.Chrome() 

driver.get("7.html")

elements = driver.find_elements(By.XPATH, "//*")  

total_elements = len(elements) 

print(f"Total number of objects on the web page: {total_elements}") 

driver.quit() 


