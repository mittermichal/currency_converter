# -*- coding: utf-8 -*-
import argparse
from forex_python.converter import CurrencyRates
import pkgutil
import json


parser = argparse.ArgumentParser(description='Currency converter.')
parser.add_argument('--amount', metavar='<float>', type=float, required=True,
                    help='amount which we want to convert - float')
parser.add_argument('--input_currency', metavar='<3 letter currency code>', required=True,
                    help='input currency - 3 letters name or currency symbol')
parser.add_argument('--output_currency', metavar='<3 letter currency code>',
                    help='requested/output currency - 3 letters name or currency symbol')


# https://github.com/MicroPyramid/forex-python/blob/80a14321ea8ecc74fc277dcd3770c685d6442cb3/forex_python/converter.py#L115
# https://github.com/MicroPyramid/forex-python/blob/9b479b76bdf05c210236550bbee47970c9e54a8c/forex_python/raw_data/currencies.json
def currency_symbol_to_code(symbol):
    if symbol == '$':
        return 'USD'
    elif symbol == '£':
        return 'GBP'
    currency_data = json.loads(pkgutil.get_data('forex_python.converter', 'raw_data/currencies.json').decode('utf-8'))
    currency_code = next((item['cc'] for item in currency_data if item["symbol"] == symbol), symbol)
    return currency_code


def convert_currency(args):

    c = CurrencyRates()

    input_currency_code = currency_symbol_to_code(args.input_currency)
    if args.output_currency:
        output_currency_code = currency_symbol_to_code(args.output_currency)
        out_currencies = {output_currency_code: (c.get_rate(input_currency_code, output_currency_code))}
    else:
        out_currencies = c.get_rates(input_currency_code)

    out_currencies_json = {k: "%.2f" % round(v*args.amount, 2) for k, v in out_currencies.items()}

    # print(args)

    output_json = {
        "input": {
            "amount": args.amount,
            "currency": input_currency_code
        },
        "output": out_currencies_json
    }
    # for symbol in '₫₹€£$¥-₪':
    #    print(currency_symbol_to_code(symbol))

    return output_json

if __name__ == '__main__':
    args = parser.parse_args()
    print(json.dumps(convert_currency(args), indent=4, sort_keys=True))
