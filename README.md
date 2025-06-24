Binance Futures Testnet Trading Bot

A Python-based automated trading bot for Binance Futures Testnet that supports placing Market, Limit, and Stop-Market orders via a simple command-line interface (CLI). Designed for educational purposes and safe experimentation in a simulated crypto trading environment.

---

## 🚀 Features

- Place Market Orders instantly at the current market price.  
- Place Limit Orders to buy/sell at a specified price.  
- Place Stop-Market Orders that trigger a market order once a stop price is reached.  
- Interactive CLI to input order details easily.  
- Detailed logging of all order activity and errors for debugging and audit trails.

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/binance-futures-testnet-trading-bot.git
cd binance-futures-testnet-trading-bot
````

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

### 1. Set up Binance API credentials

Create a `.env` file in the project root with the following content:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

> Important: Use API keys from [Binance Futures Testnet](https://testnet.binancefuture.com/) and ensure Futures Trading permission is enabled.

---

## 📁 Project Structure

```
binance-futures-testnet-trading-bot/
│
├── main.py           # CLI interface to place orders
├── bot.py            # Core Binance Futures API wrapper and order logic
├── config.py         # Loads API keys from .env environment variables
├── utils.py          # Logger setup and configuration
├── requirements.txt  # Python dependencies
└── README.md         # This documentation file
```

---

## ▶️ How to Run

Run the main script via the terminal:

```bash
python main.py
```

You will be prompted with an interactive menu to:

1. Choose an order type:

   * Market
   * Limit
   * Stop-Market
2. Input trading pair (e.g., `BTCUSDT`).
3. Choose side (`BUY` or `SELL`).
4. Specify quantity and price/stop price as applicable.

---

## 📌 Understanding Order Types

* **Market Order:** Executes immediately at the best available price.
* **Limit Order:** Executes only at the specified price or better.
* **Stop-Market Order:** Triggers a market order when the stop price is reached.

---

## 📝 Logging

* All API calls, order confirmations, and errors are logged to `logs/bot.log`.
* Logs include timestamps and detailed messages for traceability and debugging.

---

## 🧪 Binance Futures Testnet Info

* This bot operates on the official Binance Futures Testnet — a sandbox environment for developers and testers.
* Get free test funds from the [Binance Testnet Faucet](https://testnet.binancefuture.com/futures/BTCUSDT).
* URL used for API calls: `https://testnet.binancefuture.com`

---

## ⚠️ Disclaimer

This project is intended solely for educational and testing purposes.
Trading cryptocurrencies involves significant risk, and this bot should **not** be used with real funds without thorough testing and understanding.

---

## 👨‍💻 Author

Snehil Srivastava
*Built for learning and experimentation with automated crypto trading.*

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 📞 Contact

For questions or support, please reach out to [Snehil1420@gmail.com].

```
