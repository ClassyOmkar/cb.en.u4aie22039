import logging
from flask import Flask, jsonify, request

from auth_service import AuthService
from average_calculator import AverageCalculator

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_average_calculator_app(auth_service: AuthService, window_size: int = 10) -> Flask:
    """
    Create and configure the Flask app for the Average Calculator microservice.
    
    Args:
        auth_service: Authentication service for accessing the test server
        window_size: Size of the numbers window
        
    Returns:
        Configured Flask app
    """
    app = Flask("AverageCalculatorMicroservice")
    
    # Configure CORS headers manually since flask_cors is not needed
    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
        return response
    
    # Create an instance of the AverageCalculator
    calculator = AverageCalculator(auth_service, window_size=window_size)
    
    @app.route('/numbers/<string:number_id>', methods=['GET'])
    def get_numbers(number_id):
        """
        Get numbers and calculate average based on the number ID.
        
        Args:
            number_id: 'p' for prime, 'f' for Fibonacci, 'e' for even, 'r' for random
            
        Returns:
            JSON response with window states, numbers, and average
        """
        try:
            # Validate number_id
            if number_id not in calculator.number_types:
                return jsonify({"error": f"Invalid number ID. Must be one of {list(calculator.number_types.keys())}"}), 400
            
            # Calculate average and get response
            result = calculator.calculate_average(number_id)
            return jsonify(result)
        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            return jsonify({"error": str(e)}), 500
    
    # Add a basic root endpoint for health check
    @app.route('/', methods=['GET'])
    def health_check():
        return jsonify({"status": "healthy", "service": "Average Calculator"})
    
    return app