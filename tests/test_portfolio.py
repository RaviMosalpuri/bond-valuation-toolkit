from src.bond import Bond
from src.portfolio import Portfolio

def test_portfolio_metrics():
    b1 = Bond(1000, 0.05, 5, 0.03)
    b2 = Bond(1000, 0.04, 10, 0.05)
    portfolio = Portfolio([b1, b2], weights=[0.6, 0.4])

    assert portfolio.total_price() > 0
    assert portfolio.portfolio_duration() > 0
    assert portfolio.portfolio_convexity() > 0