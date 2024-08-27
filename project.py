from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Set up Chrome WebDriver (ensure you have the ChromeDriver installed and in your PATH)
driver = webdriver.Chrome()

# Search query
query = "laptop"
file = 0

# URL of Amazon search page
driver.get(f"https://www.amazon.in/s?k={query}&crid=6IQKEHY5VMR3&sprefix=laptop%2Caps%2C308&ref=nb_sb_noss_1")

# Use CSS_SELECTOR instead of CLASS_NAME to correctly handle multiple classes
elems = driver.find_elements(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline")
print(f"{len(elems)} items found")

# Ensure the 'data' directory exists
if not os.path.exists('data'):
    os.makedirs('data')

# Loop through elements and save HTML content to files
for elem in elems:
    d = elem.get_attribute("outerHTML")
    with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
        f.write(d)
    file += 1

# Close the WebDriver
driver.close()
