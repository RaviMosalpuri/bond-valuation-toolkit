import plotly.graph_objects as go
from .bond import Bond
from .portfolio import Portfolio
from .monte_carlo import monte_carlo_bond_pricing

# Example portfolio
b1 = Bond(1000, 0.05, 5, 0.03)
b2 = Bond(1000, 0.04, 10, 0.05)
portfolio = Portfolio([b1, b2], weights=[0.6, 0.4])

# Monte Carlo simulation
mean, std, prices = monte_carlo_bond_pricing(b1, num_simulations=5000, sigma=0.02, seed=123)

# Histogram of simulated prices
fig = go.Figure(data=[go.Histogram(x=prices, nbinsx=50)])
fig.update_layout(title="Monte Carlo Bond Price Distribution",
                  xaxis_title="Price", yaxis_title="Frequency")
fig.show()
