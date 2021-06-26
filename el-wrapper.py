#!/usr/bin/python3

# el-wrapper.py | jq '.'

import requests
from extractlinks import ExtractLinks as EL
# suppress warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#URL = "http://google.com/"
URL = "http://cnn.com/"

heady={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
	'Accept': 'text/html'
}

proxies = {
	'http': 'http://127.0.0.1:8888',
	'https': 'https://127.0.0.1:8888'
}

r = requests.get(URL, headers=heady, allow_redirects=True, verify=False)

e = EL(content=r)
print(e.json)
#print(e.links_all)
#for i in e.links_all:
#	print(i)
#for i in e.types_all:
#	print(i)
#for i in e.tags_all:
#	print(i)
#for i in e.attributes_all:
#	print(i)
#for d in e.urlbreakdown_generator_dict():
#	print(d)
#for j in e.urlbreakdown_generator_json():
#	print(j)