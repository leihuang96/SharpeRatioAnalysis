from matplotlib import pyplot as plt
import data_processing

def main():
    stock_data, benchmark_data = data_processing.load_data()
    stock_returns, sp_returns = data_processing.calculate_returns(stock_data, benchmark_data)
    excess_returns = data_processing.calculate_excess_returns(stock_returns, sp_returns)
    annual_sharpe_ratio = data_processing.calculate_annual_sharpe_ratio(excess_returns)
    annual_sharpe_ratio.plot.bar(title='Annualized Sharpe Ratio: Stocks vs S&P 500')

    plt.savefig('datasets/processed/annual_sharpe_ratio.png')
    plt.show()


if __name__ == "__main__":
    main()