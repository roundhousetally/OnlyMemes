#!/usr/bin/python3
import requests


def meme():
    info = requests.get('https://some-random-api.ml/meme')
    return (info.json().get('image'))
