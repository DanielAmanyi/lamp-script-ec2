import requests
import sys
import json
import ipdb

import requests
import sys


def get_bitcoin_price():
    # get bitcoin price
    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)


def main():
    # Check if the user provided the number of Bitcoins as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python bitcoin_price.py <number_of_bitcoins>")
        sys.exit(1)

    # Try to convert the argument to a float
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Error: Argument must be a number.")
        sys.exit(1)

    # Get the current Bitcoin price in USD
    price_usd = get_bitcoin_price()

    # Calculate the cost of the specified number of Bitcoins
    cost = bitcoins * price_usd

    # Output the cost, formatted with thousands separator and four decimal places
    print(f"The cost of {bitcoins} Bitcoins is: ${cost:,.4f}")


if __name__ == "__main__":
    main()
