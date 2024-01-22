import pandas as pd
import numpy as np

def load_data():
    stock_data = pd.read_csv('datasets/raw/stock_data.csv', index_col='Date', parse_dates=True).dropna()
    benchmark_data = pd.read_csv('datasets/raw/benchmark_data.csv', index_col='Date', parse_dates=True).dropna()
    return stock_data, benchmark_data

def calculate_returns(stock_data, benchmark_data):
    stock_returns = stock_data.pct_change()
    sp_returns = benchmark_data['S&P 500'].pct_change()
    return stock_returns, sp_returns

def calculate_excess_returns(stock_returns, sp_returns):
    return stock_returns.sub(sp_returns, axis=0)

def calculate_annual_sharpe_ratio(excess_returns):
    avg_excess_return = excess_returns.mean()
    sd_excess_return = excess_returns.std()
    daily_sharpe_ratio = avg_excess_return.div(sd_excess_return)
    annual_factor = np.sqrt(252)
    annual_sharpe_ratio = daily_sharpe_ratio.mul(annual_factor)
    return annual_sharpe_ratio
