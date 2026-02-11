## Step 4 — PnL calculation**
## Total PnL = cash + (inventory × current price). Track this at every step, plot it alongside price and inventory.

## Step 5 — Inventory limits**
## Add a `max_inventory` parameter. If you're too long, stop bidding. Too short, stop offering. Run it and compare PnL to the version without limits.

## **Step 1 — Price simulator**
## Write a function that generates a random walk. Start with `numpy`, use `np.random.normal()` for returns, and `np.cumsum()` to build a price path. Get comfortable plotting it with `matplotlib`.
import numpy as np
import matplotlib.pyplot as plt
import numpy.cumsum as cumsum

def generate_price_path(start_price=100, num_steps=1000, mu=0, sigma=1):
    returns = np.random.normal(mu, sigma, num_steps)
    price_path = start_price + np.cumsum(returns)
    return price_path   
price_path = generate_price_path()
plt.plot(price_path)
plt.title('Simulated Price Path')
plt.xlabel('Time Steps')
plt.ylabel('Price')
plt.show()

## Step 2 — MarketMaker class**
## Give it three pieces of state: `inventory`, `cash`, and a list of `trades`. Then write a method that takes a mid price and returns a bid and an ask (just mid ± some fixed spread).
class MarketMaker:
    def _init_(self, spread=1):
        self.inventory = 0
        self.cash = 0
        self.trades = []
        self.spread = spread
        def quote(self, mid_price):
            bid = mid_price - self.spread / 2
            ask = mid_price + self.spread / 2
            return bid, ask
        
##**Step 3 — Fill logic**
##Loop through your price series. At each step, post quotes, then check if the next price crossed your bid (you buy) or ask (you sell). Update inventory and cash accordingly.
def simulate_trading(self, price_path):
    for price in price_path:
        bid, ask = self.quote(price)
        if price <= bid: # Buy at bid
            self.inventory += 1
            self.cash -= bid
            self.trades.append(('buy', bid))
        elif price >= ask: # Sell at ask
            self.inventory -= 1
            self.cash += ask
            self.trades.append(('sell', ask))

