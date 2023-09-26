import json
from pprint import pprint
with open("secrets/secret_key.json", "r") as f:
    key = json.loads(f.read())
    pprint(key)
print("testing")