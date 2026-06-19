import numpy as np
from .bond import Bond
from .bond_pricing import price_bond

def macaulay_duration(bond: Bond):
    coupon = bond.annual_coupon()
    ytm = bond.yield_to_maturity
    n = bond.years_to_maturity
    price = price_bond(bond)

    duration = sum([
        (t * coupon) / ((1 + ytm) ** t) for t in range(1, n + 1)
    ]) + (n * bond.face_value) / ((1 + ytm) ** n)

    return duration / price

def modified_duration(bond: Bond):
    return macaulay_duration(bond) / (1 + bond.yield_to_maturity)

def convexity(bond: Bond):
    coupon = bond.annual_coupon()
    ytm = bond.yield_to_maturity
    n = bond.years_to_maturity
    price = price_bond(bond)

    convexity_val = sum([
        (coupon * t * (t+1)) / ((1 + ytm) ** (t+2)) for t in range(1, n+1)
    ]) + (bond.face_value * n * (n+1)) / ((1+ytm) ** (n+2))

    return convexity_val / price