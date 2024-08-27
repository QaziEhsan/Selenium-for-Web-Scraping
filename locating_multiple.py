from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Search query
query = "laptop"

# Access Amazon's search page with the specified query
driver.get(f"https://www.amazon.in/s?k={query}&crid=6IQKEHY5VMR3&sprefix=laptop%2Caps%2C308&ref=nb_sb_noss_1")

# Find elements by CSS selector to capture multiple classes
elems = driver.find_elements(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline")

print(f"{len(elems)} items found")

# Print the text of each found element
for elem in elems:
    print(elem.text)

# Close the browser
driver.close()
