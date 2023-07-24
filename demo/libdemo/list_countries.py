import requests

resp = requests.get("https://restcountries.com/v3.1/all")

countries = resp.json()

for c in sorted(countries, key=lambda c: c['name']['common']):
    name = c['name']['common']
    # If capital key is not found then take Unknown for capital
    capital = c.get('capital', ['Unknown'])[0]
    region = c['region']
    print(f"{name:50} {capital:30}  {region:15}")
