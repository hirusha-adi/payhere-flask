import hashlib
from flask import Flask, render_template
from flask import request, jsonify

MERCHANT_ID = '1227403'
MERCHANT_SECRET = 'Mzk2OTc5MzUxOTExODEyMTc3NjQzNzI1NjQ5MTEwMjMxNzc0MTA5OA=='

app = Flask(__name__)
app.secret_key = 'testing123'


@app.route('/', methods=['GET'])
def dashboard_user():
    return render_template(
        'index.html', 
        merchant_id=MERCHANT_ID
    )

@app.route('/generate_hash', methods=['POST'])
def payment_generate_hash():
    data = request.get_json()
    order_id = data['order_id']
    amount = format(float(data['amount']), '.2f')
    currency = data['currency']

    hash_str = (MERCHANT_ID + order_id + amount + currency + 
                hashlib.md5(MERCHANT_SECRET.encode('utf-8')).hexdigest().upper())
    hash_val = hashlib.md5(hash_str.encode('utf-8')).hexdigest().upper()

    return jsonify({'hash': hash_val})

@app.route('/notify', methods=['POST'])
def payment_notify():
    data = request.form
    merchant_id = data.get('merchant_id')
    order_id = data.get('order_id')
    payhere_amount = data.get('payhere_amount')
    payhere_currency = data.get('payhere_currency')
    status_code = data.get('status_code')
    md5sig = data.get('md5sig')
    print(request.data, "\n"*3, request.form, "\n"*3, request.args)
    hash_str = (merchant_id + order_id + payhere_amount + payhere_currency + status_code +
                hashlib.md5(MERCHANT_SECRET.encode('utf-8')).hexdigest().upper())
    local_md5sig = hashlib.md5(hash_str.encode('utf-8')).hexdigest().upper()

    if local_md5sig == md5sig and int(status_code) == 2:
        # Payment is successful, update the database accordingly
        return 'OK'
    else:
        # Payment verification failed
        return 'Error', 400

if __name__ == '__main__':
    app.run(debug=True)
    