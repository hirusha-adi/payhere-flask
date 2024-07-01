function getAttributeValue(id, attribute) {
    return document.getElementById(id).getAttribute(attribute);
}

// PayHere event handlers
payhere.onCompleted = function onCompleted(orderId) {
    console.log("Payment completed. OrderID:" + orderId);
    // Handle payment completion
};

payhere.onDismissed = function onDismissed() {
    console.log("Payment dismissed");
    // Handle payment dismissal
};

payhere.onError = function onError(error) {
    console.log("Error:" + error);
    // Handle payment error
};

// Payment data
var payment = {
    "sandbox": true,
    "merchant_id": getAttributeValue('hidden-data', 'merchant-id'),    // Replace with your Merchant ID
    "return_url": "http://localhost:5000/notify",
    "cancel_url": "http://localhost:5000/notify",
    "notify_url": "http://localhost:5000/notify",
    "order_id": "DN12345678",
    "items": "Ticket",
    "amount": getAttributeValue('hidden-data', 'user-paid-amount'),
    "currency": "LKR",
    "first_name": getAttributeValue('hidden-data', 'first-name'),
    "last_name": getAttributeValue('hidden-data', 'last-name'),
    "email": getAttributeValue('hidden-data', 'user-email'),
    "phone": getAttributeValue('hidden-data', 'user-phone'),
    "address": "No.1, Galle Road",
    "city": "Colombo",
    "country": "Sri Lanka"
};

// Generate hash value on button click
document.getElementById('payhere-payment').onclick = function () {
    fetch('/generate_hash', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            order_id: payment.order_id,
            amount: payment.amount,
            currency: payment.currency
        })
    })
        .then(response => response.json())
        .then(data => {
            payment.hash = data.hash;
            console.log(getAttributeValue('hidden-data', 'first-name'))
            payhere.startPayment(payment);
        })
        .catch(error => console.error('Error:', error));
};