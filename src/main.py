from src.data_loader import load_stock_data, load_benchmark_data

# Define file paths
stock_file_path = 'data/stock_data.csv'
benchmark_file_path = 'data/benchmark_data.csv'

# Load data
stock_data = load_stock_data(stock_file_path)
benchmark_data = load_benchmark_data(benchmark_file_path)