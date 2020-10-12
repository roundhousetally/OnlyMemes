#!/usr/bin/python3
import requests


info = requests.get('https://some-random-api.ml/meme')
print(info.json().get('image'))
