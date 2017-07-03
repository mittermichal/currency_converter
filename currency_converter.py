import argparse

parser = argparse.ArgumentParser(description='Currency converter.')
parser.add_argument('--amount', metavar='<float>', type=float, required=True,
                    help='amount which we want to convert - float')
parser.add_argument('--input_currency', metavar='<3 letter currency code>', required=True,
                    help='input currency - 3 letters name or currency symbol')
parser.add_argument('--output_currency', metavar='<3 letter currency code>',
                    help='requested/output currency - 3 letters name or currency symbol')

args = parser.parse_args()
print(args)