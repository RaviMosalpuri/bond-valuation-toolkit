import pytest
from src.bond import Bond
from src.scenario_analysis import scenario_shift

def test_scenario_analysis():
    b = Bond(face_value=1000, coupon_rate=0.05, years_to_maturity=5, yield_to_maturity=0.06)
    results = scenario_shift(b)

    assert "Base Price" in results
    assert "Price if YTM +1%" in results
    assert "Price if YTM -1%" in results

    assert results["Price if YTM +1%"] < results["Base Price"]
    assert results["Price if YTM -1%"] > results["Base Price"]