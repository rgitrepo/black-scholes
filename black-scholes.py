

"""
Underlying Price (S):   The current market price of the asset.
Strike Price (K):       The predetermined price at which the option can be exercised.
Time to Expiration (T): The time left (in years) until the option’s expiration date.
Risk Free Rate (r):     The constant rate of return on a risk-free asset, such as a government bond.
Volatility (σ):         A measure of how much the price of the underlying asset fluctuates.
"""

# Use PIP install scipy to import scipy if not already installed
import math
from scipy.stats import norm

S = 45  # Underlying Price
K = 40  # Strike Price
T = 2   # Time to Expiration
r = 0.1 # Risk-Free Rate
vol = 0.1 # Volatility (σ)

d1 = (math.log(S/K) + (r + 0.5 * vol**2)*T ) / (vol * math.sqrt(T))

d2 = d1 - (vol * math.sqrt(T))

# Call Option Price calculation
C = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

# Put Option Price calculation
P = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Print the results
print('The value of d1 is: ', round(d1, 4))
print('The value of d2 is: ', round(d2, 4))
print('The price of the call option is: $', round(C, 2))
print('The price of the put option is: $', round(P, 2))
