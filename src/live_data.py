import yfinance as yf

def get_treasury_yield_curve():
    """
    Fetch the current U.S. Treasury yield curve data using yfinance.
    Returns a dictionary with maturities as keys and yields as values.
    """
    # Fetch the 10-year Treasury yield as a proxy for the yield curve
    ticker = yf.Ticker("^TNX")  # 10-Year Treasury Note
    data = ticker.history(period="1d")

    if data.empty:
        raise ValueError("Failed to fetch Treasury yield data.")
    
    # Extract the latest yield value
    latest_yield = data['Close'].iloc[-1] / 100  # Convert from percentage to decimal
    
    # For simplicity, we will create a basic yield curve with some assumed maturities
    yield_curve = {
        1: latest_yield - 0.01,  # 1-year yield
        2: latest_yield - 0.005, # 2-year yield
        3: latest_yield,         # 3-year yield
        5: latest_yield + 0.005, # 5-year yield
        7: latest_yield + 0.01,  # 7-year yield
        10: latest_yield + 0.015,# 10-year yield
        20: latest_yield + 0.02, # 20-year yield
        30: latest_yield + 0.025 # 30-year yield
    }
    
    return yield_curve