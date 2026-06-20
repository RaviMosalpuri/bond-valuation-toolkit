from src.yield_curve import YieldCurve

def test_yield_curve_interpolation():
    maturities = [1, 2, 3, 5, 7, 10]
    yields = [0.02, 0.025, 0.03, 0.035, 0.04, 0.045]
    curve = YieldCurve(maturities, yields)

    # Test interpolation at known points
    assert abs(curve.interpolate(1) - 0.02) < 1e-6
    assert abs(curve.interpolate(2) - 0.025) < 1e-6
    assert abs(curve.interpolate(3) - 0.03) < 1e-6
    
    assert abs(curve.interpolate(5) - 0.035) < 1e-6
    assert abs(curve.interpolate(10) - 0.045) < 1e-6

    # Test interpolation between points
    assert abs(curve.interpolate(4) - 0.0325) < 1e-6  # Between 3 and 5 years
    assert abs(curve.interpolate(6) - 0.0375) < 1e-6  # Between 5 and 7 years