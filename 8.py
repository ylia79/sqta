from selenium import webdriver 

from selenium.webdriver.common.by import By 
  

driver = webdriver.Chrome() 

driver.get("check.html") 



checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']") 

checked_count = 0 

unchecked_count = 0 


for checkbox in checkboxes: 

    if checkbox.is_selected(): 

        checked_count += 1 
    else: 
        unchecked_count += 1 

number_of_checkboxes = len(checkboxes) 


print(f"Total Number of checkboxes on the page: {number_of_checkboxes}") 

print(f"Checked checkboxes: {checked_count}") 

print(f"Unchecked checkboxes: {unchecked_count}") 

driver.quit() 