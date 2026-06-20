from .bond import Bond
from .bond_pricing import price_bond

def parallel_shift(bond: Bond, shift: float):
    """Apply parallel shift to yield curve (increase/decrease YTM)."""    
    # Create a new bond with the shifted yield
    shifted_bond = Bond(
        face_value=bond.face_value,
        coupon_rate=bond.coupon_rate,
        years_to_maturity=bond.years_to_maturity,
        yield_to_maturity=bond.yield_to_maturity + shift
    )
    
    return price_bond(shifted_bond)

def scenario_shift(bond: Bond):
    base_price = price_bond(bond)
    up_shift_price = parallel_shift(bond, 0.01)  # +100 bps
    down_shift_price = parallel_shift(bond, -0.01)  # -100

    return {
        "Base Price": base_price,
        "Price if YTM +1%": up_shift_price,
        "Price if YTM -1%": down_shift_price
    }