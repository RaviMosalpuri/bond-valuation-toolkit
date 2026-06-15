from pytest import approx
from src.bond import Bond
from src.bond_pricing import price_bond

def test_pricing_bond():
    bond = Bond(face_value=1000, coupon_rate=0.05, years_to_maturity=5, yield_to_maturity=0.06)
    assert price_bond(bond) == approx(957.88, abs=1e-2)