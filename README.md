# PayHere Integration for Flask 

Flask-PayHere is a simple Flask application demonstrating how to integrate the PayHere payment gateway. It includes routes for generating payment hashes, handling payment notifications, and rendering a sample dashboard.

## Features

- Generate hash values for secure payment requests.
- Verify payment notifications from PayHere.
- Simple and easy-to-follow Flask setup.

## Prerequisites

- Python 3.8 or later
- Flask

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd flask-payhere
```

### 2. Install dependencies

Install the required Python packages using pip:

```bash
pip install flask
```

### 3. Replace sensitive information

Update the following placeholders in the code before running the application:

- **`MERCHANT_ID`**: Replace `'1227403'` with your PayHere Merchant ID.
- **`MERCHANT_SECRET`**: Replace the current secret with your actual PayHere Merchant Secret.
- **`app.secret_key`**: Change `'testing123'` to a secure random string.

**⚠️ Important:** Never expose sensitive information like your Merchant Secret or App Secret publicly.

### 4. Run the application

Start the Flask application:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000`.

## Endpoints

### 1. `GET /`

Renders the dashboard page (e.g., `index.html`). Replace this template as needed to suit your project.

### 2. `POST /generate_hash`

Generates a hash for the payment request.  
**Request payload (JSON):**

```json
{
  "order_id": "Order001",
  "amount": "100.00",
  "currency": "LKR"
}
```

**Response (JSON):**

```json
{
  "hash": "A1B2C3D4E5F6G7H8I9J0"
}
```

### 3. `POST /notify`

Handles payment notifications from PayHere. Verifies the MD5 signature and ensures the payment is successful.

**PayHere sends form data with fields like:**
- `merchant_id`
- `order_id`
- `payhere_amount`
- `payhere_currency`
- `status_code`
- `md5sig`


## Security Tips

1. **Secure your Merchant Secret:** Always store sensitive keys like `MERCHANT_SECRET` in environment variables or a secure secrets manager.  
   Example using `.env` file with [python-dotenv](https://github.com/theskumar/python-dotenv):

   ```bash
   MERCHANT_SECRET="your-secure-merchant-secret"
   ```

2. **App Secret Key:** Change the Flask app’s `secret_key` to a secure random value.

   ```python
   import os
   app.secret_key = os.urandom(24)
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This README file was generated with ChatGPT-3.5 on 1/12/25
