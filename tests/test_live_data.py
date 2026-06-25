from src.live_data import get_treasury_yield_curve

def test_get_treasury_yield_curve():
    curve = get_treasury_yield_curve()
    assert isinstance(curve, dict)
    assert all(isinstance(k, int) and isinstance(v, float) for k, v in curve.items())
    assert len(curve) > 0