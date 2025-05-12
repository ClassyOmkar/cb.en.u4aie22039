"""
Stock Price Aggregation Microservice

This microservice calculates the average price and correlation between stocks 
from an external API over a specified time window.

Usage:
    python main.py

Endpoints:
    GET /stocks - Get all available stocks
    GET /stocks/{ticker}?minutes={m}&aggregation=average - Get average stock price
    GET /stocks/correlation?minutes={m}&ticker={ticker1}&ticker={ticker2} - Get correlation
"""

import logging
from auth_service import AuthService
from app import create_stock_price_app

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    """
    Main function to run the Stock Price Aggregation microservice.
    """
    # Pre-registered credentials - you should replace these with your own
    credentials = {
        "email": "cb.en.u4aie22039@cb.students.amrita.edu",
        "name": "pathange omkareshwara rao",
        "rollNo": "cb.en.u4aie22039",
        "accessCode": "SwuuKE",
        "clientID": "a7b6195b-73c0-4c67-b49e-aee4738804fe",
        "clientSecret": "zbsnnjvDYkVBjsaq"      
    }
    
    # Create and initialize auth service
    auth_service = AuthService()
    auth_service.set_credentials(credentials)
    
    # Create and run the Flask app
    app = create_stock_price_app(auth_service)
    
    # Run the app on port 9877
    app.run(host='0.0.0.0', port=9877, debug=True)

if __name__ == "__main__":
    main()