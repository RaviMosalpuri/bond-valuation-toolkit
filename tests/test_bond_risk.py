import pytest
from src.bond import Bond
from src.bond_risk import macaulay_duration

def test_duration_convexity():
    b = Bond(face_value=1000, coupon_rate=0.05, years_to_maturity=5, yield_to_maturity=0.06)
    mac_dur = macaulay_duration(b)

    assert mac_dur > 0