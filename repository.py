import pandas as pd

from helpers_logging import log_message


def get_data():
    tickers = ["ALF1", "BET2", "GAM3", "DEL4", "EPS5"]
    log_message(f"Run Query | funds={tickers}", level="INFO")

    # Creating fake fund data
    data = {
        "Ticker": ["ALF1", "BET2", "GAM3", "DEL4", "EPS5"],
        "Fund Name": [
            "Alpha Fund",
            "Beta Fund",
            "Gamma Fund",
            "Delta Fund",
            "Epsilon Fund",
        ],
        "Asset Class": ["Equity", "Bond", "Mixed", "Real Estate", "Hedge Fund"],
        "Total AUM (in billions)": [10.5, 25.3, 12.2, 8.7, 15.4],
        "1-Year Return (%)": [12.5, 5.2, 8.0, 10.1, 15.3],
        "3-Year Return (%)": [30.0, 15.0, 22.5, 18.0, 35.0],
        "Risk Level": ["High", "Medium", "Medium", "Low", "High"],
        "Inception Year": [2010, 2015, 2012, 2008, 2017],
    }
    df = pd.DataFrame(data)
    log_message(f"Query results | data.shape={df.shape}", level="INFO")
    return df
