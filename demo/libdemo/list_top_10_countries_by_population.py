import requests

resp = requests.get("https://restcountries.com/v3.1/all")

countries = resp.json()

for c in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    name = c['name']['common']
    population = c['population']
    area = c['area']
    density = population // area
    print(f"{name:50} {population:10}  {area:10}  {density:5}")
