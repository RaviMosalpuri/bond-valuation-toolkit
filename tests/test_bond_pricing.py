from pytest import approx
from src.bond import Bond
from src.bond_pricing import price_bond, price_bond_advanced

def test_pricing_bond():
    bond = Bond(face_value=1000, coupon_rate=0.05, years_to_maturity=5, yield_to_maturity=0.06)
    assert price_bond(bond) == approx(957.88, abs=1e-2)


def test_advanced_bond_pricing():
    plain_bond = Bond(face_value=1000, coupon_rate=0.05, years_to_maturity=5, yield_to_maturity=0.06)
    price = price_bond_advanced(plain_bond)
    assert price == approx(957.88, abs=1e-2)

    callable_bond = Bond(face_value=1000, coupon_rate=0.05, years_to_maturity=5, yield_to_maturity=0.06, callable=True)
    price = price_bond_advanced(callable_bond)
    assert price > 0

    puttable_bond = Bond(face_value=1000, coupon_rate=0.05, years_to_maturity=5, yield_to_maturity=0.06, puttable=True)
    price = price_bond_advanced(puttable_bond)
    assert price > 0

    zero_coupon_bond = Bond(face_value=1000, coupon_rate=0.0, years_to_maturity=5, yield_to_maturity=0.06)
    zero_coupon_price = price_bond_advanced(zero_coupon_bond)
    assert zero_coupon_price == approx(747.26, abs=1e-2)