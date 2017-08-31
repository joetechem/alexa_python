import json
import requests

filename = 'sites.json'
with open(filename) as f_obj:
    sites_list = json.load(f_obj)
print(sites_list)


