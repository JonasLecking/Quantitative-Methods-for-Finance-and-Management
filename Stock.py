import Configuration.Stock as config
import datetime as dt
import mplfinance as mpf
import statistics as stats
import numpy as np

from Option import Option
from datetime import datetime as dtdt

class Stock():

    def __init__(self, ticker):
        self.ticker = ticker
        
        if config.should_get_stock_price:
            try:
                self.price_history = config.get_stock_price(ticker)
            except:
                print("Error: Price history could not be retrieved for symbol" + ticker + ". Check the following: \n- In Configuration.Stock, should_get_price_history is enabled \n- The get_stock_price function works properly and returns an output in the correct format \n-The API key in Configuration.Stock is valid \nYou can find Configuration.Stock at this location: ")
                
        if config.should_get_company_information:
            try:
                self.information = config.get_company_information(ticker)
            except:
                print("Add error code.")
        
        if config.should_get_intraday:
            try:
                self.intraday = config.get_intraday(ticker)
            except:
                print("Add error code.")

        if config.should_get_news:
            try:
                self.news = config.get_news(ticker)
            except:
                print("Add error code.")

        if config.should_get_statistics:
            try:
                self.statistics = config.get_statistics(ticker)
            except:
                print("Add error code.")

        if config.should_get_financials_and_valuation:
            try:
                self.financials, self.valuation = config.get_financials_and_valuation(ticker)
            except:
                print("Add error code.")

    def plot(self, candlestick=True, include_volume=True, moving_average=(7)):
        if candlestick:
            if include_volume:
                mpf.plot(self.price_history,type="candle",mav=moving_average,volume=True, show_nontrading=False)
            else:
                mpf.plot(self.price_history,type="candle",mav=moving_average,volume=False, show_nontrading=False)
        else:
            if include_volume:
                mpf.plot(self.price_history,type="line",mav=moving_average,volume=True, show_nontrading=False)
            else:
                mpf.plot(self.price_history,type="line",mav=moving_average,volume=False, show_nontrading=False)
        

    def plot_intraday():
        pass 

    def price(self):
        return self.price_history["Close"][0]
        
    def last_open(self):
        return self.price_history["Open"][0]

    def last_close(self):
        return self.price_history["Close"][0]

    def last_low(self):
        return self.price_history["Low"][0]

    def last_high(self):
        return self.price_history["High"][0]

    def last_volume(self):
        return self.Price_history["Volume"][0]

    def average_volume(self, ema=True):
        if ema:
            return self.price_history["Volume"].reversed().ewm(span=len(self.price_history)/30, adjust=False)[-1]
        else:
            date_3_mo_prior_to_last = config.end_date - dt.timedelta(months=3)
            length = len(self.price_history.index.loc[:date_3_mo_prior_to_last])
            volumes = self.price_history["Volume"][:length]
            return (sum(volumes)/len(volumes))

    def daily_volatility(self):
        price_history = self.price_history
        price_history["Daily Change"] = self.price_history["Close"][::-1].pct_change()
        return stats.stdev(price_history["Daily Change"].to_list()[:252])

    def annualized_volatility(self):
        return self.daily_volatility() * np.sqrt(252)
        
    def option(self, strike_price, expiration_date, risk_free_rate):
        return Option(self.ticker, strike_price, expiration_date, self.price_history["Close"][0], self.annualized_volatility(), risk_free_rate)


    

    

    
