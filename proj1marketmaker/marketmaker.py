## Market Maker Simulation
## Step 1 — Price simulator
## Write a function that generates a random walk. Start with `numpy`, use `np.random.normal()` for returns, and `np.cumsum()` to build a price path. Get comfortable plotting it with `matplotlib`.
import numpy as np
import matplotlib.pyplot as plt

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

## Step 2 + 3 — MarketMaker class + Fill logic
## Give it three pieces of state: `inventory`, `cash`, and a list of `trades`. Then write a method that takes a mid price and returns a bid and an ask (just mid ± some fixed spread).
class MarketMaker:
    def __init__(self, spread=1):
        self.inventory = 0
        self.cash = 0
        self.trades = []
        self.spread = spread
    def quote(self, mid_price):
            bid = mid_price - self.spread / 2
            ask = mid_price + self.spread / 2
            return bid, ask
    def simulate_trading(self, price_path):
        for i in range(len(price_path) - 1):
            bid, ask = self.quote(price_path[i])
            next_price = price_path[i + 1]
            if next_price <= bid: # Buy at bid
                    self.inventory += 1
                    self.cash -= bid
                    self.trades.append(('buy', bid))
            elif next_price >= ask: # Sell at ask
                    self.inventory -= 1
                    self.cash += ask
                    self.trades.append(('sell', ask))
    def calculate_pnl(self, current_price):
        return self.cash + self.inventory * current_price
    def plot_results(self, price_path):
        pnl_path = []
        for price in price_path:
            plt.figure(figsize=(12, 6))
            plt.subplot(2, 1, 1)
            plt.plot(price_path, label='Price')
            plt.title('Price Path')
            plt.xlabel('Time Steps')
            plt.ylabel('Price')
            plt.legend()
            plt.subplot(2, 1, 2)
            plt.title('PnL Path')
            plt.xlabel('Time Steps')
            plt.ylabel('PnL')
            plt.legend()
            plt.tight_layout()
            plt.show()      
    def max_inventory_check(self, price):
        if self.inventory >= self.max_inventory:
            return False # Stop bidding
        elif self.inventory < -self.max_inventory:
            return False # Stop offering 
        return True # Continue quoting
    
# Example usage
mm = MarketMaker(spread=1)
mm.simulate_trading(price_path)
current_price = price_path[-1]
pnl = mm.calculate_pnl(current_price)
print(f'Final Inventory: {mm.inventory}')
print(f'Final Cash: {mm.cash}')
print(f'Final PnL: {pnl}')
mm.plot_results(price_path)