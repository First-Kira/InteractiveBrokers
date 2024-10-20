import requests
import time
from datetime import datetime

# Replace these with your actual credentials
API_KEY = 'YOUR_API_KEY@AMER.OAUTHAP'
ACCOUNT_ID = 'YOUR_ACCOUNT_ID'
GME_SYMBOL = 'GME'
QUANTITY = 10

def buy_stock():
    url = f'https://api.tdameritrade.com/v1/accounts/{ACCOUNT_ID}/orders'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    order_data = {
        "orderType": "LIMIT",
        "session": "NORMAL",
        "duration": "DAY",
        "orderStrategyType": "SINGLE",
        "orderLegs": [{
            "instruction": "BUY",
            "quantity": QUANTITY,
            "instrument": {
                "symbol": GME_SYMBOL,
                "assetType": "EQUITY"
            }
        }],
        "price": get_current_price()  # You may need to define a function to get the current price
    }
    
    response = requests.post(url, headers=headers, json=order_data)
    if response.status_code == 201:
        print("Order placed successfully!")
    else:
        print("Failed to place order:", response.json())

def get_current_price():
    # Implement a function to get the current market price for GME
    pass

while True:
    now = datetime.now()
    if now.hour == 13 and now.minute == 6:  # 1:06 PM
        buy_stock()
        time.sleep(60)  # Sleep for a minute to avoid multiple orders in the same minute
    time.sleep(1)  # Check every second

