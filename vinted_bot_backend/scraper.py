from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin 
app = Flask(__name__)
CORS(app, support_credentials=True)

# Specify the path to the ChromeDriver
DRIVER_PATH = "/Users/joepdekock/Documents/sem7/Vinted bot/vinted_bot_backend/chromedriver"
item_data = []  

def scrapeData():
    #item_data = [] 
    try:
        # Create a Service instance
        service = Service(DRIVER_PATH)
        # Initialize WebDriver with the service
        driver = webdriver.Chrome(service=service)
        # Navigate to the URL
        driver.get('https://www.vinted.nl/catalog?search_text=&brand_ids[]=77600&brand_ids[]=289223&brand_ids[]=113926&brand_ids[]=109048&brand_ids[]=54661&brand_ids[]=344945&brand_ids[]=80700&brand_ids[]=1435462&search_id=19165114934&order=newest_first&time=1733411034')
        
        # Wait for the element to be visible
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "feed-grid"))
        )
        items = driver.find_elements(By.CLASS_NAME, 'feed-grid__item')
        # Print the element for debugging
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all(class_='u-position-relative u-min-height-none u-flex-auto')
        for item in items:
            itemLink = item.find(class_='new-item-box__overlay new-item-box__overlay--clickable')
            itemImage = item.find(class_='web_ui__Image__content')
            itemPrice = item.find(class_='web_ui__Text__text web_ui__Text__subtitle web_ui__Text__left web_ui__Text__clickable web_ui__Text__underline-none')
            print(itemLink.get('href'))
            print(itemImage.get('src'))
            print(itemLink.get('title'))
            itemdata = {
                'imageSRC': itemImage.get('src'),
                'imageTitle': itemLink.get('title'),
                'imageLink': itemLink.get('href')
            }
            item_data.append(itemdata)
    finally:
        # It's a good practice to close the browser when done
        driver.quit()
        return item_data
   

@app.route('/scrape', methods=['GET'])
@cross_origin(origin='*')
def getData():
    scrapeData()
    data = scrapeData()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
