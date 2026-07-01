import argparse
import os
from dotenv import load_dotenv
from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import validate_order
from bot.logging_config import setup_logging

def show_balance(client):
    account_info = client.get_account_info()
    balances = account_info['assets']
    print("=== Account Balances ===")
    for asset in balances:
        wallet = float(asset['walletBalance'])
        available = float(asset['availableBalance'])
        if wallet > 0 or available > 0:
            print(f"{asset['asset']}: Wallet={wallet}, Available={available}")

def show_positions(client):
    account_info = client.get_account_info()
    positions = account_info['positions']
    print("=== Open Positions ===")
    for pos in positions:
        amt = float(pos['positionAmt'])
        if amt != 0:
            print(f"{pos['symbol']}: Position={amt}, Entry={pos['entryPrice']}, PnL={pos['unrealizedProfit']}")

def main():
    logger = setup_logging()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")
    parser.add_argument("--symbol", help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for LIMIT)")
    parser.add_argument("--balance", action="store_true", help="Check account balance")
    parser.add_argument("--positions", action="store_true", help="Check open positions")
    args = parser.parse_args()

   
    load_dotenv()
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    client = BinanceClient(api_key, api_secret)
    order_manager = OrderManager(client)

    if args.balance:
        show_balance(client)
        return

    if args.positions:
        show_positions(client)
        return

    try:
        validate_order(args.type, args.price)
    except ValueError as e:
        print(f"Input Error: {e}")
        return

    try:
        if args.type == "MARKET":
            response = order_manager.place_market_order(args.symbol, args.side, args.quantity)
        else:
            response = order_manager.place_limit_order(args.symbol, args.side, args.quantity, args.price)

        print("=== Order Request Summary ===")
        print(f"Symbol: {args.symbol}, Side: {args.side}, Type: {args.type}, Quantity: {args.quantity}, Price: {args.price}")
        print("=== Order Response Details ===")
        print(response)

        logger.info(f"Order placed successfully: {response}")

    except Exception as e:
        print(f"Order failed: {e}")
        logger.error(f"Order failed: {e}")

if __name__ == "__main__":
    main()
