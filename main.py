import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

resp = requests.get("https://appbrewery.github.io/Zillow-Clone/")
content = BeautifulSoup(resp.text, "html.parser")
all_prices = content.find_all(class_="PropertyCardWrapper__StyledPriceLine")
price_list = []
for price in all_prices:
    price_list.append(price.text[:6])

address_list = []
links_list = []

all_addresses = content.find_all(class_="StyledPropertyCardDataArea-anchor")
for address in all_addresses:
    address_list.append(address.getText().strip().replace("|", ""))
    links_list.append(address.get('href'))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://forms.gle/wWryydZxtv6zxHQb7")
driver.maximize_window()

for num in range(len(all_prices)):
    time.sleep(2)
    form_inputs = driver.find_elements(by=By.CLASS_NAME, value="whsOnd")
    submit_button = driver.find_element(by=By.CLASS_NAME, value="NPEfkd")
    form_inputs[0].click()
    form_inputs[0].send_keys(address_list[num])
    form_inputs[1].send_keys(price_list[num])
    form_inputs[2].send_keys(links_list[num])
    submit_button.click()
    time.sleep(2)
    driver.back()
