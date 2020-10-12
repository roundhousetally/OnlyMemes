#!/usr/bin/python3
import requests
info = requests.get('https://api.thecatapi.com/v1/images/search')
print(info.json()[0].get('url'))
