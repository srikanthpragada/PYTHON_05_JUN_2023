from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)

soup = BeautifulSoup(resp.text, 'html.parser')

links = []
for link in soup.find_all("a"):
    href = link['href']
    if href == '#':
        continue

    if not href.startswith("http"):
        if href.startswith("/"):
            href = WEBSITE + href
        else:
            href = WEBSITE + "/" + href

    if href not in links:
        links.append(href)

for link in links:
    print(link)
