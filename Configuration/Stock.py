import datetime as dt
import pandas as pd
import requests as rq
import json as js
import time as tm
import numpy as np

from datetime import datetime as dtdt

# This script contains configuration options for the Stock class.
# - Variables in this file, for example the start and end date between which
#   the stock's price history should be retrieved, can be altered during runtime
# - All functions in this file, for example the function which retrieves the
#   stock's price history, can be altered when the script is not running. The
#   output required from the function is defined in the comments within the
#   function's code
# - This way, you can fit your own data sources if necessary

api_key = "br0k98nrh5radq31k030"

end_date = dtdt.today() # Date at which stock price history ends
start_date = end_date - dt.timedelta(days=365*3) # Date at which stock price history begins

should_get_stock_price = True # If enabled, sript will attempt to retrieve stock price history
should_get_company_information = True # If enabled, sript will attempt to retrieve company information
should_get_intraday = True # If enabled, sript will attempt to retrieve intraday price history
should_get_news = True
should_get_statistics = True
should_get_financials_and_valuation = True

error_output_enabled = True # If enabled, any of the below functions NOT working properly will result in a warning output, but no runtime error

def get_stock_price(symbol):

    # Alter function to use your own data source! Output format:
    # Pandas DataFrame with the following structure
    # - Index: date of the stock price as datetime object,
    #          ordered from last date to earliest date
    # - Columns:
    #   - Open, Close, Low, High: all of type float
    #   - Volume: of type int

    url = 'https://finnhub.io/api/v1/stock/candle?symbol=' + symbol + '&resolution=D&token=' + api_key

    if start_date != None or end_date != None:
        from_tt = tm.mktime(start_date.timetuple())
        to_tt = tm.mktime(end_date.timetuple())
        url = 'https://finnhub.io/api/v1/stock/candle?symbol=' + symbol + '&resolution=D&from=' + str(int(from_tt)) + '&to=' + str(int(to_tt)) + '&token=' + api_key

    r = rq.get(url)
    df = pd.DataFrame()
    resp_json = r.json()
    
    df["Close"] = resp_json["c"][::-1]
    df["Open"] = resp_json["o"][::-1]
    df["High"] = resp_json["h"][::-1]
    df["Low"] = resp_json["l"][::-1]
    df["Volume"] = resp_json["v"][::-1]

    dates_raw = resp_json["t"][::-1]
    dates = []

    for each in dates_raw:
        dates.append(dtdt.fromtimestamp(each))

    df["date"] = dates
    df.set_index("date", inplace=True)

    return df 

def get_company_information(symbol):
    pass

def get_intraday(symbol):
    pass

def get_news(symbol):
    pass

def get_statistics(symbol):
    # EPS, Dividend yield, 
    
    pass

def get_financials_and_valuation(symbol):
    # Key values from each financial statement, if possible
    
    pass


    
    
