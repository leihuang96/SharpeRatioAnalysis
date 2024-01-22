import sys
import os
import unittest
from unittest.mock import patch

# Calculate the path to the src directory and add it to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import main
from data_handler import load_stock_data
from data_handler import load_benchmark_data

class TestMain(unittest.TestCase):
    @patch('main.load_stock_data')
    @patch('main.load_benchmark_data')
    @patch('main.calculate_daily_returns')
    @patch('main.calculate_excess_returns')
    @patch('main.calculate_sharpe_ratio')
    @patch('matplotlib.pyplot.show')
    def test_main(self, mock_show, mock_calculate_sharpe_ratio, mock_calculate_excess_returns,
                  mock_calculate_daily_returns, mock_load_benchmark_data, mock_load_stock_data):
        # Mock the necessary functions and data
        mock_load_stock_data.return_value = [1, 2, 3, 4, 5]
        mock_load_benchmark_data.return_value = [2, 3, 4, 5, 6]
        mock_calculate_daily_returns.return_value = [0.1, 0.2, 0.3, 0.4, 0.5]
        mock_calculate_excess_returns.return_value = [0.05, 0.15, 0.25, 0.35, 0.45]
        mock_calculate_sharpe_ratio.return_value = 1.0

        # Call the necessary functions
        mock_load_stock_data.assert_called_once()
        mock_load_benchmark_data.assert_called_once()
        mock_calculate_daily_returns.assert_called_once()
        mock_calculate_excess_returns.assert_called_once()
        mock_calculate_sharpe_ratio.assert_called_once()
        mock_show.assert_called_once()

        # Call the main function
        main()

if __name__ == '__main__':
    unittest.main()
