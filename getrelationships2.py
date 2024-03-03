from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

target = sys.argv[1]

# Setup WebDriver (Example with Chrome)
driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed

# Navigate to the website's home page to establish a session
driver.get('https://builtwith.com')

# Add your session cookie
cookie = {'name': 'BWSSON', 'value': sys.argv[2]}
driver.add_cookie(cookie)

# Now navigate to the target URL
target_url = f'https://builtwith.com/relationships/{target}'
driver.get(target_url)

# Wait for the elements to load (adjust the XPath or CSS selector as needed)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//td[@class="hbomb"]/a'))
)

# Execute JavaScript to scrape data
javascript_query = """
var elements = document.querySelectorAll('td.hbomb a'); // Adjust the CSS selector as needed
return Array.from(elements).map(element => element.textContent.trim());
"""
results = driver.execute_script(javascript_query)

for result in results:
    print(result)

driver.quit()