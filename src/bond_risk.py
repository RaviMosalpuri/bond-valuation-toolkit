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