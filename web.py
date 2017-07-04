from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse
from currency_converter import convert_currency

errors = {
    'RatesNotAvailableError': {
        'message': "Rate for this currency not available",
        'status': 422,
    },
}

app = Flask(__name__)
api = Api(app, errors=errors)

req_parser = reqparse.RequestParser()
req_parser.add_argument('amount', type=float, required=True)
req_parser.add_argument('input_currency', required=True)
req_parser.add_argument('output_currency')


class CurrencyConverter(Resource):
    def get(self):
        args = req_parser.parse_args()
        #print(args)
        return jsonify(convert_currency(args))


api.add_resource(CurrencyConverter, '/currency_converter')

if __name__ == '__main__':
    app.run(debug=False)
