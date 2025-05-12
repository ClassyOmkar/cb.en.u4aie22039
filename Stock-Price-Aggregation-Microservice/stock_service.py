import time
import logging
import numpy as np
import requests
from typing import List, Dict, Any, Optional, Union

from auth_service import AuthService

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class StockService:
    def __init__(self, auth_service: AuthService):
        self.base_url = "http://20.244.56.144/evaluation-service"
        self.auth_service = auth_service
        self.cache = {}  # Cache to store stock data and reduce API calls
        self.cache_expiry = {}  # Store cache expiry time for each ticker
        
    def get_stocks(self) -> Dict[str, str]:
        """
        Get all stocks listed on the stock exchange.
        
        Returns:
            Dictionary mapping stock names to ticker symbols
        """
        url = f"{self.base_url}/stocks"
        token = self.auth_service.get_token()
        headers = {"Authorization": f"Bearer {token}"}
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data.get("stocks", {})
            else:
                logger.error(f"Error fetching stocks: {response.status_code} - {response.text}")
                return {}
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching stocks: {str(e)}")
            return {}
    
    def get_stock_price(self, ticker: str, minutes: Optional[int] = None) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Get the price history of a stock for the specified time window.
        
        Args:
            ticker: Stock ticker symbol
            minutes: Time window in minutes (optional)
            
        Returns:
            List of price history entries or single price data
        """
        # Check cache first
        cache_key = f"{ticker}_{minutes}"
        current_time = time.time()
        
        # If cached data exists and hasn't expired, return it
        if cache_key in self.cache and self.cache_expiry.get(cache_key, 0) > current_time:
            return self.cache[cache_key]
        
        # Build API URL based on whether minutes is specified
        url = f"{self.base_url}/stocks/{ticker}"
        if minutes is not None:
            url += f"?minutes={minutes}"
        
        token = self.auth_service.get_token()
        headers = {"Authorization": f"Bearer {token}"}
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                
                # Cache the result for 30 seconds to minimize API calls
                self.cache[cache_key] = data
                self.cache_expiry[cache_key] = current_time + 30  # 30 seconds cache time
                
                return data
            else:
                logger.error(f"Error fetching stock price: {response.status_code} - {response.text}")
                return {}
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching stock price for {ticker}: {str(e)}")
            return {}
    
    def calculate_average_price(self, ticker: str, minutes: int) -> Dict[str, Any]:
        """
        Calculate the average price of a stock over the specified time window.
        
        Args:
            ticker: Stock ticker symbol
            minutes: Time window in minutes
            
        Returns:
            Dictionary with average price and price history
        """
        try:
            # Get price history for the specified time window
            price_history = self.get_stock_price(ticker, minutes)
            
            # Handle different response formats
            if isinstance(price_history, dict) and "stock" in price_history:
                # Single price point response
                price_data = [price_history["stock"]]
                avg_price = price_data[0]["price"]
            elif isinstance(price_history, list):
                # Multiple price points response
                price_data = price_history
                if not price_data:
                    return {"averageStockPrice": 0, "priceHistory": []}
                avg_price = sum(item["price"] for item in price_data) / len(price_data)
            else:
                logger.error(f"Unexpected response format for ticker {ticker}")
                return {"averageStockPrice": 0, "priceHistory": []}
            
            # Format the response
            return {
                "averageStockPrice": avg_price,
                "priceHistory": price_data
            }
        except Exception as e:
            logger.error(f"Error calculating average price for {ticker}: {str(e)}")
            return {"averageStockPrice": 0, "priceHistory": []}
    
    def calculate_correlation(self, ticker1: str, ticker2: str, minutes: int) -> Dict[str, Any]:
        """
        Calculate the correlation between two stocks' price movements.
        
        Args:
            ticker1: First stock ticker symbol
            ticker2: Second stock ticker symbol
            minutes: Time window in minutes
            
        Returns:
            Dictionary with correlation coefficient and stock data
        """
        try:
            # Get price data for both stocks
            stock1_data = self.calculate_average_price(ticker1, minutes)
            stock2_data = self.calculate_average_price(ticker2, minutes)
            
            # Extract price history
            stock1_prices = [item["price"] for item in stock1_data.get("priceHistory", [])]
            stock2_prices = [item["price"] for item in stock2_data.get("priceHistory", [])]
            
            # Calculate correlation using NumPy
            if len(stock1_prices) <= 1 or len(stock2_prices) <= 1:
                # Cannot calculate correlation with insufficient data
                correlation = 0
            else:
                # Use NumPy's corrcoef to calculate Pearson correlation coefficient
                # If lengths are different, calculate correlation based on the available data points
                min_length = min(len(stock1_prices), len(stock2_prices))
                correlation_matrix = np.corrcoef(stock1_prices[:min_length], stock2_prices[:min_length])
                correlation = correlation_matrix[0, 1]
                
                # Handle potential NaN values (could occur if one of the arrays has constant values)
                if np.isnan(correlation):
                    correlation = 0
            
            # Format response
            return {
                "correlation": round(correlation, 4),  # Round to 4 decimal places
                "stocks": {
                    ticker1: stock1_data,
                    ticker2: stock2_data
                }
            }
        except Exception as e:
            logger.error(f"Error calculating correlation between {ticker1} and {ticker2}: {str(e)}")
            return {"correlation": 0, "stocks": {ticker1: {}, ticker2: {}}}