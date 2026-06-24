from src.bond_pricing import price_bond
from src.bond_risk import macaulay_duration, modified_duration, convexity

class Portfolio:
    def __init__(self, bonds, weights=None):
        self.bonds = bonds
        if weights is None:
            self.weights = [1 / len(bonds)] * len(bonds)
        else:
            self.weights = weights

    def total_price(self):
        return sum(w * price_bond(b) for b, w in zip(self.bonds, self.weights))

    def portfolio_duration(self):
        return sum(w * modified_duration(b) for b, w in zip(self.bonds, self.weights))

    def portfolio_convexity(self):
        return sum(w * convexity(b) for b, w in zip(self.bonds, self.weights))