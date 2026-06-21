import numpy as np
from .bond import Bond
from .bond_pricing import price_bond

def monte_carlo_bond_pricing(bond: Bond, num_simulations=10000, sigma=0.02, seed=None):
    """
    Monte Carlo simulation for bond pricing.
    
    Parameters:
    - bond: Bond object
    - num_simulations: Number of simulations to run
    - sigma: Standard deviation of the yield changes (volatility)
    - seed: Random seed for reproducibility
    
    Returns:
    - mean_price: Mean price from simulations
    - std_dev_price: Standard deviation of prices from simulations
    """
    if seed is not None:
        np.random.seed(seed)
    
    simulated_prices = []
    
    for _ in range(num_simulations):
        # Simulate a random change in yield using a normal distribution
        shock = np.random.normal(0, sigma)
        simulated_yield = bond.yield_to_maturity + shock
        
        # Create a new bond with the simulated yield
        simulated_bond = Bond(
            face_value=bond.face_value,
            coupon_rate=bond.coupon_rate,
            years_to_maturity=bond.years_to_maturity,
            yield_to_maturity=simulated_yield
        )
        
        # Price the simulated bond and store the result
        price = price_bond(simulated_bond)
        simulated_prices.append(price)
    
    mean_price = np.mean(simulated_prices)
    std_dev_price = np.std(simulated_prices)
    
    return mean_price, std_dev_price, simulated_prices


def value_at_risk(simulated_prices, confidence_level=0.95):
    """
    Calculate Value at Risk (VaR) from simulated bond prices.
    
    Parameters:
    - simulated_prices: List of simulated bond prices
    - confidence_level: Confidence level for VaR calculation (default is 95%)
    
    Returns:
    - var: Value at Risk at the specified confidence level
    """
    sorted_prices = np.sort(simulated_prices)
    index = int((1 - confidence_level) * len(sorted_prices))
    var = sorted_prices[index]
    
    return var


def expected_shortfall(simulated_prices, confidence_level=0.95):
    """
    Calculate Expected Shortfall (ES) from simulated bond prices.
    
    Parameters:
    - simulated_prices: List of simulated bond prices
    - confidence_level: Confidence level for ES calculation (default is 95%)
    
    Returns:
    - es: Expected Shortfall at the specified confidence level
    """
    sorted_prices = np.sort(simulated_prices)
    index = int((1 - confidence_level) * len(sorted_prices))
    es = np.mean(sorted_prices[:index])
    
    return es