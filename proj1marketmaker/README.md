# Market Maker Simulation

A Python-based market maker simulator that models the behavior of an algorithmic market maker trading against a simulated price path.

## Overview

This project implements a simplified market maker that:
- Generates realistic price paths using random walks
- Quotes bid/ask prices with configurable spreads
- Simulates trading based on price movements
- Tracks inventory and cash positions
- Calculates and visualizes profit & loss (PnL)

## Features

### Price Generation
- **Random Walk Simulation**: Generates realistic price paths using normal distribution returns
- **Customizable Parameters**: Control starting price, number of steps, volatility (sigma), and drift (mu)

### Market Maker Logic
- **Quote Generation**: Returns bid and ask prices based on a configurable spread
- **Trading Simulation**: Automatically buys and sells based on price movements relative to quotes
- **Inventory Management**: Enforces maximum inventory limits to prevent over-exposure
- **Position Tracking**: Maintains detailed records of all trades and current positions

### Analytics
- **PnL Calculation**: Real-time profit & loss based on current inventory and cash
- **Visualization**: Plots price path and PnL evolution over time

## Components

### `generate_price_path()`
Generates a simulated price path using geometric Brownian motion principles.

**Parameters:**
- `start_price` (float): Initial price (default: 100)
- `num_steps` (int): Number of time steps (default: 1000)
- `mu` (float): Drift/mean return (default: 0)
- `sigma` (float): Volatility (default: 1)

**Returns:** NumPy array of prices

### `MarketMaker` Class

#### Attributes:
- `inventory`: Current number of units held
- `cash`: Current cash position
- `trades`: List of all executed trades
- `spread`: Bid-ask spread width
- `max_inventory`: Maximum allowed inventory position

#### Methods:

**`quote(mid_price)`**
Returns bid and ask prices around the mid price.

**`simulate_trading(price_path)`**
Simulates trading against the price path. Buys when price falls below bid, sells when price rises above ask.

**`calculate_pnl(current_price)`**
Calculates current profit/loss as: `cash + (inventory × current_price)`

**`plot_results(price_path)`**
Creates a two-panel visualization showing price path and PnL evolution.

**`max_inventory_check(price)`**
Returns `False` if inventory limits are reached, preventing over-exposure.

## Usage

```python
# Create a price path
price_path = generate_price_path(start_price=100, num_steps=1000, sigma=1)

# Initialize market maker with 1-unit spread
mm = MarketMaker(spread=1)

# Simulate trading
mm.simulate_trading(price_path)

# Check results
current_price = price_path[-1]
pnl = mm.calculate_pnl(current_price)
print(f'Final Inventory: {mm.inventory}')
print(f'Final Cash: {mm.cash}')
print(f'Final PnL: {pnl}')

# Visualize
mm.plot_results(price_path)
```

## Requirements

- `numpy`: Numerical computing
- `matplotlib`: Plotting and visualization

## Dependencies

Install required packages:
```bash
pip install numpy matplotlib
```

## Example Output

The simulation produces:
- Console output showing final inventory, cash, and PnL
- Two-panel plot showing:
  - **Top panel**: Simulated price path
  - **Bottom panel**: Market maker's PnL over time

## Future Enhancements

- Adaptive spreads based on volatility
- Order queue simulation
- Risk metrics (Sharpe ratio, max drawdown)
- Parameter optimization
- Multi-asset market making
