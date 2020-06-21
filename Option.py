import datetime as dt
import enum
import numpy as np
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf

from datetime import datetime as dtdt

class ValuationType(enum.Enum):
    black_scholes = 1
    binomial = 2
    trinomial = 3

class Option():

    def __init__(self, ticker, strike_price, expiration_date, spot_price, volatility, risk_free_rate, call=True):
        self.ticker = ticker
        self.strike_price = strike_price
        self.expiration_date = expiration_date
        self.volatility = volatility
        self.spot_price = spot_price
        self.call = call
        self.r = risk_free_rate

    def intrinsic_value(valuation_type=ValuationType.black_scholes):
        if valuation_type == ValuationType.black_scholes:
            T = (expiration_date - dtdt.today()).days
            return black_scholes(self.spot_price, self.strike_price, T, self.r, self.volatility, call=self.call)
        elif valuation_type == binomial:
            return binomial()
        elif valuation_type == trinomial:
            return trinomial()
        
    def implied_volatility(price):
        pass

    def black_scholes(self, S, K, T, r, sigma, call):
        if call:
            d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
            d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
            call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
            return call
        else:
            d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
            d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
            put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
            return put

    def __binomial():
        pass

    def __trinomial():
        pass 

    def break_even_analysis(price):
        pass
