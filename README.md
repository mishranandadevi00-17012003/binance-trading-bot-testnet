##### PROJECT STRUCTURE

trading_bot/
    bot/
      init.py
      client.py        → Binance client wrapper
      orders.py        → Order placement logic
      validators.py    → Input validation
      logging_config.py
cli.py             → CLI entry point
requirements.txt
.env.example
README.md
/////////////////////////////////////////////////////////////////////////////////////////////////

#####SETUP INSTRUCTIONS

Create and activate a virtual environment
Run: python -m venv .venv

Activate it:
Windows (PowerShell): .venv\Scripts\activate
Mac/Linux: source .venv/bin/activate

Install dependencies
Run: pip install -r requirements.txt

Configure environment variables

Ceate a .env file in the project root with:
API_KEY=your_testnet_api_key_here
API_SECRET=your_testnet_secret_key_here

Use .env.example as a template.

Run the bot

se the CLI commands below to place orders or check account info.
/////////////////////////////////////////////////////////////////////////////////////////////////////////////

##### EXAMPLE
Place a Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Place a Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

Check Account Balance:
python cli.py --balance

Check Open Positions:
python cli.py --positions

Check Open Orders:
python cli.py --orders --symbol BTCUSDT
///////////////////////////////////////////////
##### FEATURES

Connects securely to Binance Futures Testnet

Places Market and Limit orders (BUY/SELL)

Validates order inputs

Logs all activity to trading_bot.log

CLI flags for balance, positions, and open orders

Exception handling for invalid input, API errors, and network failures

Deliverables
