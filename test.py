from urllib.request import urlopen

import dload as dload

def get_currency_price(val, valute_1, valute_2):
    url = str(
        'https://free.currconv.com/api/v7/convert?q=' + valute_1 + '_' + valute_2 + '&compact=ultra&apiKey=1498fdd2b22d0458536e')
    j = dload.json(url)
    return j[val]


print(get_currency_price('USD_RUB', 'USD', 'RUB'))
