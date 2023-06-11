from flask import Flask, request, jsonify
import requests
app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    cf = fetch_conversion_factor(source_currency, target_currency, amount)
    final_amount = cf
    final_amount = round(final_amount,2)
    print(final_amount)
    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount, target_currency, final_amount, source_currency)
    }
    return jsonify(response)
def fetch_conversion_factor(source,target,amnt):
    url = "https://api.apilayer.com/fixer/convert?to={}&from={}&amount={}".format(source, target, amnt)
    headers = {
        "apikey": "IXcrc0580d7QAzP8NR7qyIpHqFaMJH1p"
    }
    response = requests.get(url, headers=headers)
    response = response.json()
    return response['result']

if __name__ == "__main__":
    app.run(debug=True)
