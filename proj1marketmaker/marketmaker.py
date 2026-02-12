import numpy as np
import matplotlib.pyplot as plt

def generate_price_path(start_price=100, num_steps=1000, mu=0, sigma=3):
    returns = np.random.normal(mu, sigma, num_steps)
    price_path = start_price + np.cumsum(returns)
    return price_path

class MarketMaker:
    def __init__(self, spread=3, max_inventory=20):
        self.inventory = 0
        self.cash = 0
        self.trades = []
        self.spread = spread
        self.max_inventory = max_inventory

    def calculate_recent_vol(self, price_path, i, window=20):
        if i < 2:
            return 1.0
        if i < window:
            return np.std(np.diff(price_path[:i+1]))
        return np.std(np.diff(price_path[i-window:i]))

    def quote(self, mid_price, recent_vol):
        dynamic_spread = self.spread + 2 * recent_vol
        bid = mid_price - dynamic_spread / 2
        ask = mid_price + dynamic_spread / 2
        return bid, ask

    def simulate_trading(self, price_path):
        for i in range(len(price_path) - 1):
            recent_vol = self.calculate_recent_vol(price_path, i)
            bid, ask = self.quote(price_path[i], recent_vol)
            next_price = price_path[i + 1]
            if next_price <= bid and self.inventory < self.max_inventory:
                self.inventory += 1
                self.cash -= bid
                self.trades.append(('buy', bid))
            elif next_price >= ask and self.inventory > -self.max_inventory:
                self.inventory -= 1
                self.cash += ask
                self.trades.append(('sell', ask))

    def calculate_pnl(self, current_price):
        return self.cash + self.inventory * current_price

    def plot_results(self, price_path):
        pnl_path = []
        for price in price_path:
            pnl = self.calculate_pnl(price)
            pnl_path.append(pnl)
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 1, 1)
        plt.plot(price_path, label='Price')
        plt.title('Price Path')
        plt.xlabel('Time Steps')
        plt.ylabel('Price')
        plt.legend()
        plt.subplot(2, 1, 2)
        plt.plot(pnl_path, label='PnL', color='orange')
        plt.title('PnL Path')
        plt.xlabel('Time Steps')
        plt.ylabel('PnL')
        plt.legend()
        plt.tight_layout()
        plt.show()

price_path = generate_price_path()
mm = MarketMaker(spread=3, max_inventory=20)
mm.simulate_trading(price_path)
print(f'Final Inventory: {mm.inventory}')
print(f'Final PnL: {mm.calculate_pnl(price_path[-1]):.2f}')
print(f'Trades: {len(mm.trades)}')
mm.plot_results(price_path)