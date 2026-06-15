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