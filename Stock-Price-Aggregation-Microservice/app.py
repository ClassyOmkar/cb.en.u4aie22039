import logging
from flask import Flask, jsonify, request

from auth_service import AuthService
from stock_service import StockService

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_stock_price_app(auth_service: AuthService) -> Flask:
    """
    Create and configure the Flask app for the Stock Price Aggregation microservice.
    
    Args:
        auth_service: Authentication service for accessing the test server
        
    Returns:
        Configured Flask app
    """
    app = Flask("StockPriceAggregationMicroservice")
    
    # Configure CORS headers manually
    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
        return response
    
    # Create an instance of the StockService
    stock_service = StockService(auth_service)
    
    @app.route('/stocks', methods=['GET'])
    def get_stocks():
        """
        Get all stocks listed on the stock exchange.
        
        Returns:
            JSON response with stock names and ticker symbols
        """
        try:
            stocks = stock_service.get_stocks()
            return jsonify({"stocks": stocks})
        except Exception as e:
            logger.error(f"Error fetching stocks: {str(e)}")
            return jsonify({"error": str(e)}), 500
    
    @app.route('/stocks/<string:ticker>', methods=['GET'])
    def get_stock_average(ticker):
        """
        Get the average stock price in the last 'm' minutes.
        
        Query Parameters:
            minutes: Time window in minutes
            aggregation: Type of aggregation (currently only 'average' is supported)
            
        Returns:
            JSON response with average stock price and price history
        """
        try:
            minutes = request.args.get('minutes', type=int)
            aggregation = request.args.get('aggregation', 'average')
            
            if minutes is None:
                return jsonify({"error": "Missing required parameter: minutes"}), 400
            
            if aggregation.lower() != 'average':
                return jsonify({"error": "Unsupported aggregation type. Only 'average' is supported."}), 400
            
            result = stock_service.calculate_average_price(ticker, minutes)
            return jsonify(result)
        except Exception as e:
            logger.error(f"Error calculating average price for {ticker}: {str(e)}")
            return jsonify({"error": str(e)}), 500
    
    @app.route('/stocks/correlation', methods=['GET'])
    def get_stock_correlation():
        """
        Get the correlation between two stocks' price movements in the last 'm' minutes.
        
        Query Parameters:
            minutes: Time window in minutes
            ticker: Stock ticker symbols (must be specified exactly twice)
            
        Returns:
            JSON response with correlation coefficient and stock data
        """
        try:
            minutes = request.args.get('minutes', type=int)
            tickers = request.args.getlist('ticker')
            
            if minutes is None:
                return jsonify({"error": "Missing required parameter: minutes"}), 400
            
            if len(tickers) != 2:
                return jsonify({"error": "Exactly 2 ticker parameters must be provided"}), 400
            
            result = stock_service.calculate_correlation(tickers[0], tickers[1], minutes)
            return jsonify(result)
        except Exception as e:
            logger.error(f"Error calculating correlation: {str(e)}")
            return jsonify({"error": str(e)}), 500
    
    # Add a basic root endpoint for health check
    @app.route('/', methods=['GET'])
    def health_check():
        return jsonify({"status": "healthy", "service": "Stock Price Aggregation"})
    
    return app