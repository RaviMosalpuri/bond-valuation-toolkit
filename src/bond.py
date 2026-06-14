class Bond:
    def __init__(self, face_value: float, coupon_rate: float, years_to_maturity: int, yield_to_maturity: float):
        """
        Initialize a bond.
        face_value: Principal repayment at maturity
        coupon_rate: Annual coupon rate (%)
        years_to_maturity: Remaining years until maturity
        yield_to_maturity: Market discount rate (%)
        """
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.years_to_maturity = years_to_maturity
        self.yield_to_maturity = yield_to_maturity

    def annual_coupon(self):
        """Calculate annual coupon payment."""
        return self.face_value * self.coupon_rate