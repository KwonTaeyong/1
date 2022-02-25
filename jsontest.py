import json
from pprint import pprint

with open('DELIVERY_READY.json', 'r') as f:
    json_data = json.load(f)
pprint(json_data)
