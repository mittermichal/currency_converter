# -*- coding: utf-8 -*-
import argparse
from forex_python.converter import CurrencyCodes
import json

parser = argparse.ArgumentParser(description='Currency converter.')
parser.add_argument('--amount', metavar='<float>', type=float, required=True,
                    help='amount which we want to convert - float')
parser.add_argument('--input_currency', metavar='<3 letter currency code>', required=True,
                    help='input currency - 3 letters name or currency symbol')
parser.add_argument('--output_currency', metavar='<3 letter currency code>',
                    help='requested/output currency - 3 letters name or currency symbol')

#args = parser.parse_args()

#https://github.com/MicroPyramid/forex-python/blob/80a14321ea8ecc74fc277dcd3770c685d6442cb3/forex_python/converter.py#L115
#https://github.com/MicroPyramid/forex-python/blob/9b479b76bdf05c210236550bbee47970c9e54a8c/forex_python/raw_data/currencies.json
def currency_symbol_to_code(symbol):
    if symbol=='$':
        return 'USD'
    elif symbol=='£':
        return 'GBP'
    with open('currencies.json') as f:
        currency_data = json.loads(f.read())
    currency_dict = next((item['cc'] for item in currency_data if item["symbol"] == symbol), None)
    return currency_dict

#print(args)
for symbol in '₫₹€£$¥-₪':
    print(currency_symbol_to_code(symbol))