import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load  data

def load_stock_data(file_path):
    return pd.read_csv(file_path, parse_dates=['Date'], index_col='Date', dtype={'Date': 'datetime64'}).dropna()

def load_benchmark_data(file_path):
    return pd.read_csv(file_path, parse_dates=['Date'], index_col='Date', dtype={'Date': 'datetime64'}).dropna()
