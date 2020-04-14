# Imports
import requests
import json


def change_url(url):
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    return parsed


def get_currency_price(url, val):
    return change_url(url)[val]['rate']


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def sum(currencies, fun):
    sums = currencies * float(fun)
    return str(toFixed(sums, 2))

