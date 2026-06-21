import numpy as np
import matplotlib.pyplot as plt

class YieldCurve:
    def __init__(self, maturities, yields):
        """
        maturities: list of maturities in years
        yields: list of yields corresponding to maturities
        """
        self.maturities = np.array(maturities)
        self.yields = np.array(yields)

    def interpolate(self, maturity):
        """Linear interpolation for yield at given maturity."""
        return np.interp(maturity, self.maturities, self.yields)