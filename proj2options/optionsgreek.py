## **Step 1 — Understand what Black-Scholes calculates**
## It answers one question: "What is a fair price for an option right now?" It takes 5 inputs: current stock price (S), strike price (K), time to expiry (T), risk-free rate (r), and volatility (sigma). It outputs a price for a call and a put.
## **Step 2 — Implement the formula**
## The formula uses two values called d1 and d2:
#   `d1 = (ln(S/K) + (r + sigma²/2) * T) / (sigma * sqrt(T))`
#   `d2 = d1 - sigma * sqrt(T)`
#   `call_price = S * N(d1) - K * e^(-rT) * N(d2)`
#   `put_price = K * e^(-rT) * N(-d2) - S * N(-d1)`
# Where `N()` is the normal CDF. Use `np.log` for ln, `np.exp` for e, `np.sqrt` for sqrt, and `from scipy.stats import norm` then `norm.cdf()` for N().

# **Step 3 — Calculate the Greeks**
# These tell you how the option price changes when inputs change. Start with delta (sensitivity to price) and vega (sensitivity to vol). Google the formulas when you get here.

# **Step 4 — Plot how price changes as you vary each input**
# Make a chart showing call price vs stock price for different volatilities. Then call price vs time to expiry. This builds visual intuition.
# **Start with steps 1 and 2.** Write a function `black_scholes(S, K, T, r, sigma)` that returns call and put prices. Test it with S=100, K=100, T=1, r=0.05, sigma=0.2 — you should get a call price around $10.45.

import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

from scipy.stats import norm
def black_scholes(S, K, T, r, sigma):
    d1= (np.log(S/K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T)) 
    d2= d1 - sigma * np.sqrt(T) 
    call_price= S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2) 
    put_price= K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1) 
    return call_price, put_price

# Test the function
S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2
call_price, put_price = black_scholes(S, K, T, r, sigma)
print(f"Call Price: {call_price:.2f}, Put Price: {put_price:.2f}")

# Calculating the Greeks
def delta (S, K, T, r, sigma): 
    d1 = (np.log(S/K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    return norm.cdf(d1)
def vega(S, K, T, r, sigma): 
    d1 = (np.log(S/K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    return S * norm.pdf(d1) * np.sqrt(T)

delta_value = delta(S, K, T, r, sigma)
vega_value = vega(S, K, T, r, sigma) 
print(f"Delta: {delta_value:.4f}, Vega: {vega_value:.4f}")

# Plotting how price changes as you vary each input
S_values = np.linspace(50, 150, 100) 
call_prices = [black_scholes(S, K, T, r, sigma)[0] for S in S_values] 
for sig in [0.1, 0.2, 0.3]:
    call_prices_sig = [black_scholes(S, K, T, r, sig)[0] for S in S_values] 
    plt.plot(S_values, call_prices_sig, label=f'Volatility={sig}')
plt.figure(figsize=(10, 6)) 
plt.plot(S_values, call_prices, label='Call Price') 
plt.title('Call Price vs Stock Price') 
plt.xlabel('Stock Price (S)') 
plt.ylabel('Call Price') 
plt.legend() 
plt.grid() 
plt.show()

T_values = np.linspace(0.01, 2, 100) 
call_prices_T = [black_scholes(S, K, T, r, sigma)[0] for T in T_values] 
plt.figure(figsize=(10, 6)) 
plt.plot(T_values, call_prices_T, label='Call Price') 
plt.title('Call Price vs Time to Expiry') 
plt.xlabel('Time to Expiry (T)') 
plt.ylabel('Call Price') 
plt.legend() 
plt.grid() 
plt.show()