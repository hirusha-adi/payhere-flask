import hashlib
import json

def create_payment(name, price):
    order_id = "1234"
    merchant_id = "111111"
    currency = "LKR"
    merchant_secret = "MzU2NTA5OTMxMzI4NjQzMzE5MzMxMT"
    hash_value = hashlib.md5(
        (merchant_id + order_id + format(float(price), '.2f') + currency + 
         hashlib.md5(merchant_secret.encode('utf-8')).hexdigest()).encode('utf-8')
    ).hexdigest().upper()

    return {
        'order_id': order_id,
        'merchant_id': merchant_id,
        'name': name,
        'price': price,
        'currency': currency,
        'hash': hash_value
    }

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_payment():
    data = request.form
    response = create_payment(data['name'], data['price'])
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
