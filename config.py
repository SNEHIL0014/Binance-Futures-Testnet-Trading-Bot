import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
BASE_URL = "https://testnet.binancefuture.com"

# Optional: Safety check (warn if keys are missing)
if not API_KEY or not API_SECRET:
    raise EnvironmentError("❌ API_KEY or API_SECRET not found in .env file.")
