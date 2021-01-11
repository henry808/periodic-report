#!/usr/bin/env python3

import requests, os

response = requests.get('https://api.github.com')

print(response.status_code)
print(response.text)

file_dir = os.path.dirname(__file__)
file_name = "data.txt"

file_path = os.path.join(file_dir, file_name)

with open(file_path, "w") as f:
	f.write(response.text)