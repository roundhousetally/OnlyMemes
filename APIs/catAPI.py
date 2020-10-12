#!/usr/bin/python3
import requests


def cat():
    info = requests.get('https://api.thecatapi.com/v1/images/search')
    return (info.json()[0].get('url'))
