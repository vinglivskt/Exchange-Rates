# Imports
from urllib.request import urlopen

import requests
import json
import dload as dload


# def change_url(url):
#     response = requests.get(url)
#     data = response.text
#     parsed = json.loads(data)
#     return parsed
#
#
# def get_currency_price(url, val):
#     return change_url(url)[val]['rate']


def get_currency_price(val):
    try:
        url = str(
        'https://free.currconv.com/api/v7/convert?q='+val+'&compact=ultra&apiKey=1498fdd2b22d0458536e')
        j = dload.json(url)
        return j[val]
    except KeyError:
        url = str(
            'https://free.currconv.com/api/v7/convert?q=' + val + '&compact=ultra&apiKey=1498fdd2b22d0458536e')
        j = dload.json(url)
        return j[val]
    


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def sum(currencies, fun):
    sums = currencies * float(fun)
    return str(toFixed(sums, 2))
