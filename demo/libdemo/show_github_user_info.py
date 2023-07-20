import requests

resp = requests.get("https://api.github.com/users/srikanthpragada")

#print(resp.status_code)   # 200, 404
#print(resp.headers['content-type'])
if resp.status_code == 200:
    details = resp.json()   # convert response(json) to dict
    print(details['name'])
    print(details['company'])
    print(details['location'])
else:
    print("Sorry! Could not get details. Error :", resp.text)