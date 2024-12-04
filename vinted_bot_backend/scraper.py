from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to the ChromeDriver
DRIVER_PATH = "/Users/joepdekock/Documents/sem7/Vinted bot/vinted_bot_backend/chromedriver"

# Create a Service instance
service = Service(DRIVER_PATH)

# Initialize WebDriver with the service
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the URL
    driver.get('https://www.vinted.nl/catalog')
    
    # Wait for the element to be visible
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "feed-grid__item--one-fifth"))
    )
    h1 = driver.find_elements(By.CLASS_NAME, 'feed-grid__item--one-fifth')
    # Print the element for debugging
    for h1 in h1:
        print(h1.text)
    
finally:
    # It's a good practice to close the browser when done
    driver.quit()
