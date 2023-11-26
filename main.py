# Import necessary libraries
from time import sleep
import libarbitrage
from dotenv import load_dotenv
import os

# Load environmental variables from .env file
load_dotenv()

# Set variables to pass as arguments
APIKEY = os.getenv("INFURA_APIKEY")
tokens = ['eth', 'btc', 'ftt', 'aave', 'usdc', 'usdt']  # Tokens to analyze between
revenue = 1.5  # Minimum amount of revenue in percentage per one USDT

# A single function starts and manages all the process of arbitrage analyze.
libarbitrage.arbitrage(APIKEY=APIKEY, tokens=tokens, min_revenue=revenue)

# After a while (depending on the number of tokens specified),
# we are able to retrieve the result of arbitrage analyze respectively:
arbitrage_data = libarbitrage.getArbitrageData()

# Now you can process or do whatever you want with the data.
# Let's see which blocks are analyzed so far.
print(arbitrage_data.keys())

# Get the last key's value from the arbitrage_data dictionary:
last_key = list(arbitrage_data)[-1]
data = arbitrage_data.get(last_key)

# Print formatted data
libarbitrage.printFormattedData(data)
