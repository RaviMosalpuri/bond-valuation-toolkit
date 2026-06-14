# Bond Valuation Toolkit

## Project Overview
The Bond Valuation Toolkit is a Python-based framework designed to calculate and analyze the fair value of fixed-income securities. It implements discounted cash flow (DCF) methods for plain vanilla bonds and provides a foundation for more advanced features such as yield curve modeling, duration, and convexity analysis.

This project aligns with the CFA curriculum by reinforcing fixed-income valuation concepts and risk measures, while also serving as a practical resource for quantitative finance applications.

## Project Goals
- Automate bond pricing using discounted cash flow techniques.
- Provide modular code for extending into advanced valuation methods.
- Demonstrate CFA-relevant applications such as yield-to-maturity, duration, and convexity.
- Build a structured, testable, and extensible codebase suitable for quantitative finance projects.
- Offer Jupyter Notebook demonstrations for educational and professional use.

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- GitHub account for version control and project hosting

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bond-valuation-toolkit.git
   cd bond-valuation-toolkit
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure
```
bond-valuation-toolkit/
├── src/           # Python scripts (bond class, pricing functions)
├── notebooks/     # Jupyter notebooks for demos and analysis
├── data/          # Sample bond data
├── tests/         # Unit tests
├── docs/          # Documentation and references
├── README.md      # Project overview and instructions
└── requirements.txt
```

## Usage
Run the bond pricing script to calculate the price of a plain vanilla bond:
```bash
python src/bond_pricing.py
```

Example (5-year bond, 5% coupon, 1000 face value, 6% yield-to-maturity):
```bash
Bond Price: 957.35
```
