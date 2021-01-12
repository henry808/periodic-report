#!/usr/bin/env python3

import requests, os, pprint, time


response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

print(response.status_code)

timestr = time.strftime("-%Y-%m-%d--%H-%M")

file_dir = os.path.dirname(__file__)
file_name = "data" + timestr + ".txt"

file_path = os.path.join(file_dir, file_name)

pretty_text = pprint.pformat(response.text, indent=4)

with open(file_path, "w") as f:
	f.write(pretty_text)