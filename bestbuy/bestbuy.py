import requests
from requests_html import HTMLSession

searchUrl = (
    "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
)

try:
    session = HTMLSession()
    soldOutButton = session.get(searchUrl).html.find("button", containing="sold out")
    print("Ready to Order" if (not soldOutButton) else "The ps5 is sold out right now")

except requests.exceptions.RequestException as e:
    print(e)
