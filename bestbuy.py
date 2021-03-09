import requests
from chromedriver_py import binary_path
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

baseUrl = "https://bestbuy.com/"

driver = webdriver.Chrome(executable_path=binary_path)
driver.get(baseUrl)

modal_close_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".widgets-view-email-modal .c-modal-grid .c-close-icon")
    )
)

print("Closing modal...")

modal_close_button.click()

search_bar = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@placeholder='Search Best Buy']"))
)

print("typing into search bar...")
search_bar.click()
search_bar.send_keys("ps5 console")

search_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@title='submit search']"))
)
print("clicking enter for search...")
search_button.click()
searchUrl = driver.current_url

try:
    session = HTMLSession()
    search_response = session.get(searchUrl)
    selection = "h4 > a"
    ps5_link = search_response.html.find(selection, first=True).absolute_links.pop()
    print(ps5_link)
    soldOutButton = session.get(ps5_link).html.find("button", containing="sold out")
    print("Ready to Order" if (not soldOutButton) else "The ps5 is sold out right now")

except requests.exceptions.RequestException as e:
    print(e)
