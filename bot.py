from binance.client import Client
from binance.enums import *
from config import API_KEY, API_SECRET
from utils import setup_logger

class BasicBot:
    def __init__(self, api_key=API_KEY, api_secret=API_SECRET, testnet=True):
        self.logger = setup_logger()

        if testnet:
            self.client = Client(api_key, api_secret, testnet=True)
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        else:
            self.client = Client(api_key, api_secret)

        self.logger.info(f"Client initialized (Testnet={testnet})")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            self.logger.info(f"Market Order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=str(price)
            )
            self.logger.info(f"Limit Order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Error placing limit order: {e}")
            return None

    def place_stop_market_order(self, symbol, side, quantity, stop_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type=ORDER_TYPE_STOP_MARKET,
                stopPrice=str(stop_price),
                quantity=quantity,
                timeInForce=TIME_IN_FORCE_GTC
            )
            self.logger.info(f"Stop-Market Order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Error placing stop-market order: {e}")
            return None
