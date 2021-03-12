import requests
from requests_html import HTMLSession

searchUrl = (
    "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
)

try:
    session = HTMLSession()
    isOrderable = session.get(searchUrl).html.find("button", containing="Add to Cart")
    print("Ready to Order" if (isOrderable) else "The ps5 is sold out right now")

except requests.exceptions.RequestException as e:
    print(e)
