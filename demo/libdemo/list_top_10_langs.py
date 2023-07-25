from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.tiobe.com/tiobe-index/"
resp = requests.get(WEBSITE)

soup = BeautifulSoup(resp.text, 'html.parser')
try:
    table = soup.find(id = 'top20')
    tbody = table.find("tbody")

    for row in tbody.find_all("tr")[:10]:
        cols = row.find_all("td")
        name = cols[4].text
        rating =cols[5].text
        print(f"{name:20}  {rating:5}")
except Exception as ex:
    print('Error -->', ex )
