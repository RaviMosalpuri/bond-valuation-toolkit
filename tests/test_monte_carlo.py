from src.bond import Bond
from src.monte_carlo import monte_carlo_bond_pricing, value_at_risk, expected_shortfall

def test_monte_carlo():
    b = Bond(face_value=1000, coupon_rate=0.05, years_to_maturity=5, yield_to_maturity=0.06)
    mean_price, std_dev_price, simulated_prices = monte_carlo_bond_pricing(b, num_simulations=1000, sigma=0.02, seed=42)

    assert mean_price > 0
    assert std_dev_price > 0
    assert len(simulated_prices) == 1000

    value_at_risk_95 = value_at_risk(simulated_prices, confidence_level=0.95)
    expected_shortfall_95 = expected_shortfall(simulated_prices, confidence_level=0.95)
    assert value_at_risk_95 < mean_price
    assert expected_shortfall_95 < mean_price