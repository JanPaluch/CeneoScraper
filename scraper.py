import requests
product_code = "62290435"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
print(response.status_code)