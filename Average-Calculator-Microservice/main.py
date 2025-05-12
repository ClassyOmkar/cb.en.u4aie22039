"""
Average Calculator Microservice

This microservice calculates the average of numbers fetched from an external API.
It maintains a window of unique numbers and responds with the state before and after the API call.

Usage:
    python main.py

Endpoints:
    GET /numbers/{number_id} - Get numbers and calculate average
        - number_id: 'p' for prime, 'f' for Fibonacci, 'e' for even, 'r' for random
"""

import logging
from auth_service import AuthService
from app import create_average_calculator_app

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    """
    Main function to run the Average Calculator microservice.
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
    app = create_average_calculator_app(auth_service, window_size=10)
    
    # Run the app on port 9876 as specified in the test case
    app.run(host='0.0.0.0', port=9876, debug=True)

if __name__ == "__main__":
    main()