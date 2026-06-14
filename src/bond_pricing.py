import numpy as np
from bond import Bond

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

if __name__ == "__main__":
    # Example: 5-year bond, 5% coupon, 1000 face value, 6% YTM
    b = Bond(face_value=1000, coupon_rate=0.05, years_to_maturity=5, yield_to_maturity=0.06)
    print("Bond Price:", round(price_bond(b), 2))