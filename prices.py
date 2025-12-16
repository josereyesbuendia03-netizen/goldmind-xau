import requests
from config import PRICE_API_KEY

def get_xau_price():
    url = f"https://api.twelvedata.com/price?symbol=XAU/USD&apikey={PRICE_API_KEY}"
    r = requests.get(url).json()
    return float(r["price"])
