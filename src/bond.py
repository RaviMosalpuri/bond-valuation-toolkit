class Bond:
    def __init__(self, face_value: float, coupon_rate: float, years_to_maturity: int, yield_to_maturity: float,
                 callable: bool = False, puttable: bool = False, credit_spread: float = 0.0, default_probability: float = 0.0,
                 recovery_rate: float = 0.4):
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
        self.callable = callable
        self.puttable = puttable
        self.credit_spread = credit_spread
        self.default_probability = default_probability
        self.recovery_rate = recovery_rate

    def annual_coupon(self):
        """Calculate annual coupon payment."""
        return self.face_value * self.coupon_rate