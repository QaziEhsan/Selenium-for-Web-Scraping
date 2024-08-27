from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Search query
query = "laptop"

# Access Amazon's search page with the specified query
driver.get(f"https://www.amazon.in/s?k={query}&crid=6IQKEHY5VMR3&sprefix=laptop%2Caps%2C308&ref=nb_sb_noss_1")

# Use CSS_SELECTOR instead of CLASS_NAME to correctly handle multiple classes
elem = driver.find_element(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline")

# Print the outer HTML of the found element
print(elem.get_attribute("outerHTML"))

# Wait for 20 seconds
time.sleep(20)

# Close the browser
driver.close()
