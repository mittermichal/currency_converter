# Currency converter

## Installation

`pip install -r requirements.txt`

## Usage

```
python currency_converter.py [-h] --amount <float> --input_currency <3 letter
                             currency code>
                             [--output_currency <3 letter currency code>]
```

## Parameters
- `amount` - amount which we want to convert - float
- `input_currency` - input currency - 3 letters name or currency symbol
- `output_currency` - requested/output currency - 3 letters name or currency symbol; if its missing, convert to all known currencies

## WebAPI
`python web.py`
```
GET /currency_converter?amount=0.9&input_currency=¥&output_currency=AUD HTTP/1.1
{   
    "input": {
        "amount": 0.9,
        "currency": "CNY"
    },
    "output": {
        "AUD": 0.20, 
    }
}
```