from flask import Flask, render_template, request, redirect, url_for, session
import random
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

IPG_BASE_URL = "https://sandbox.payhere.lk/pay/checkout"
IPG_BASE_URL_SAND = "https://sandbox.payhere.lk/pay/checkout"

@app.route('/')
def index():
    return render_template('index.html', base_url=IPG_BASE_URL_SAND)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        session['form_data'] = form_data
        return redirect(url_for('checkout'))

    order_id = random.randint(10000, 99999)
    session_id = session.sid
    return render_template('checkout.html', order_id=order_id, session_id=session_id, base_url=IPG_BASE_URL)

@app.route('/checkout-response')
def checkout_response():
    # Handle the response from PayHere
    return "Checkout response received"

@app.route('/checkout-notify', methods=['POST'])
def checkout_notify():
    # Handle the notification from PayHere
    data = request.form.to_dict()
    # Process the notification data
    return "Notification received"

if __name__ == '__main__':
    app.run(debug=True)
