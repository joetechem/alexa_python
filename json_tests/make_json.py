import json
import requests

sites_url = 'https://wva-dev.sosdata.org/sites.json'
r2 = requests.get(sites_url)
sites_list = r2.json()

filename = 'sites.json'
with open(filename, 'w') as f_obj:
    json.dump(sites_list, f_obj)
