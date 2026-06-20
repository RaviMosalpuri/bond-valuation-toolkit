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

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.maturities, self.yields, marker='o')
        plt.title('Yield Curve')
        plt.xlabel('Maturity (Years)')
        plt.ylabel('Yield (%)')
        plt.grid()
        plt.show()