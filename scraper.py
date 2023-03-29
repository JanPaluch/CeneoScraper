import requests
from bs4 import BeautifulSoup
product_code = "62290435"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, "html.parser")
print(page_dom.prettify())