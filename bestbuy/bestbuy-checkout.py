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
search_bar.send_keys("demon souls")
search_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@title='submit search']"))
)

print("clicking enter for search...")
search_button.click()

add_to_cart_button = driver.find_elements_by_class_name("add-to-cart-button")[0]

data_sku_id = add_to_cart_button.get_attribute('data-sku-id')

print("clicking add to cart...")
add_to_cart_button_clickable = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, f"//button[@data-sku-id='{data_sku_id}']")
    )
)

add_to_cart_button_clickable.click()

print("going to cart...")
goto_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[@href='/cart']")
    )
)
print(goto_cart_button.text)
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
input_email.send_keys("")

input_password = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[@type='password']")
    )
)

input_password.click()
input_password.send_keys("")

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
cvv_input.send_keys("")

print("Placing Order...")
place_order_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "button__fast-track")
    )
)

place_order_button.click()


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