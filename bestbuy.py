import time

import requests
from requests_html import AsyncHTMLSession, HTMLSession
from selenium import webdriver
from selenium.webdriver.support.ui import Select

baseUrl = "https://bestbuy.com/"

driver = webdriver.Chrome()
driver.get(baseUrl)

if driver.find_element_by_class_name("c-close-icon"):
    driver.find_element_by_class_name("c-close-icon").click()

searchBar = driver.find_element_by_tag_name("input").send_keys("ps5 console")
driver.find_element_by_class_name("header-search-button").click()
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
