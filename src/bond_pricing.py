import numpy as np
from .bond import Bond

def price_bond(bond: Bond):
    """
    Price a plain vanilla bond using Discounted Cash Flow (DCF).
    """
    coupon = bond.annual_coupon()
    ytm = bond.yield_to_maturity
    n = bond.years_to_maturity

    # Discount coupon payments
    coupon_pv = sum([coupon /((1 + ytm) ** t) for t in range(1, n+1)])

    # Discount face value
    face_pv = bond.face_value / ((1 + ytm) ** n)

    return coupon_pv + face_pv


def price_bond_advanced(bond: Bond):
    """
    Price a bond considering credit risk and other features.
    """
    ytm = bond.yield_to_maturity + bond.credit_spread
    coupon = bond.face_value * bond.coupon_rate
    n = bond.years_to_maturity

    # Discounted cash flows
    coupon_pv = sum([coupon / ((1 + ytm) ** t) for t in range(1, n + 1)])
    face_pv = bond.face_value / ((1 + ytm) ** n)
    price = coupon_pv + face_pv

    # Default risk adjustment
    expected_recovery = bond.recovery_rate * bond.face_value
    adjusted_price = price * (1 - bond.default_probability) + expected_recovery * bond.default_probability

    if bond.callable:
        # If callable, assume the bond will be called at the first opportunity
        call_price = bond.face_value  # Assuming call price is face value
        adjusted_price = min(adjusted_price, call_price)
    if bond.puttable:
        # If puttable, assume the bondholder will put the bond at the first opportunity
        put_price = bond.face_value  # Assuming put price is face value
        adjusted_price = max(adjusted_price, put_price)

    return adjusted_price