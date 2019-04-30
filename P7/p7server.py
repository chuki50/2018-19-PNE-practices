import requests
import sys

server = "http://rest.ensembl.org"
ext = "/sequence/id"
headers = {"Content-Type": "application/json", "Accept": "application/json"}
r = requests.post(server + ext, headers=headers, data='{ "ids" : ["ENSG00000157764", "ENSG00000248378" ] }')

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()
print(repr(decoded))
