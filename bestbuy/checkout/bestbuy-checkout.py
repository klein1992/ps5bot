import os
import time

import requests
from chromedriver_py import binary_path
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

baseUrl = "https://www.bestbuy.com/site/demons-souls-standard-edition-playstation-5/6430152.p?skuId=6430152"

# "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
# chrome_options.add_argument('--blink-settings=imagesEnabled=false')

start_time = time.time()
driver = webdriver.Chrome(executable_path=binary_path, options=chrome_options)
driver.get(baseUrl)

print("clicking add to cart...")
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "add-to-cart-button")
    )
)

add_to_cart_button.click()

print("going to cart...")
goto_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/cart']")
    )
)
goto_cart_button.click()

print("checking out...")
checkout_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-track='Checkout - Top']")
    )
)

checkout_button.click()

print("verifying age...")
age_verification_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "age-verification__button")
    )
)

age_verification_button.click()

print("entering info...")
input_email = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[@type='email']")
    )
)

input_email.click()
input_email.send_keys(os.getenv('EMAIL'))

input_password = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[@type='password']")
    )
)

input_password.click()
input_password.send_keys(os.getenv('PASSWORD'))

print("Logging in...")
sign_in_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[@data-track='Sign In']")
    )
)

sign_in_button.click()

print("Entering cvv...")

cvv_input = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.ID, "credit-card-cvv")
    )
)

cvv_input.click()
cvv_input.send_keys(os.getenv('CVV'))

print("Placing Order...")
place_order_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "button__fast-track")
    )
)

place_order_button.click()