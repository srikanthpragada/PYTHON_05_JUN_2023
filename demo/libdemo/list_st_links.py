from bs4 import BeautifulSoup
import requests

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)

soup = BeautifulSoup(resp.text, 'html.parser')

links = []
for link in soup.find_all("a"):
    href= link['href']
    if href == '#':
        continue

    if not href.startswith("http"):
        href = WEBSITE + "/" + href

    if href not in links:
         links.append(href)


for link in links:
     print(link)