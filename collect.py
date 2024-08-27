from bs4 import BeautifulSoup
import os

# Initialize a dictionary to store extracted data
data = {"title": [], "price": [], "link": []}

# Directory containing the HTML files
data_dir = "data"

# Loop through all files in the 'data' directory
for file in os.listdir(data_dir):
    # Construct the full file path
    file_path = os.path.join(data_dir, file)
    
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        html_doc = f.read()
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    # Find the first <h2> element and get its text
    title_element = soup.find("h2")
    
    if title_element:
        title = title_element.get_text(strip=True)
        print(title)  # Print the extracted title for debugging
        
        # Store the extracted title in the dictionary
        data["title"].append(title)
    
    # Optional: extract other elements such as price and link
    # For example:
    # price_element = soup.find("span", class_="price")
    # link_element = soup.find("a", href=True)
    
    # You can add these extractions similarly and store them in the dictionary
    
    # Print the prettified HTML content (optional)
    # print(soup.prettify())

# Print the final dictionary with all extracted data
print(data)
