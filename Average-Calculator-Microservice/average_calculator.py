import logging
import requests
from typing import List, Dict, Any

from auth_service import AuthService

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class AverageCalculator:
    def __init__(self, auth_service: AuthService, window_size: int = 10):
        self.window_size = window_size
        self.numbers_window = []  # Using a simple list for more explicit control
        self.base_url = "http://20.244.56.144/evaluation-service"
        self.number_types = {
            'p': 'primes',           # Prime numbers
            'f': 'fibo',             # Fibonacci numbers
            'e': 'even',             # Even numbers
            'r': 'rand'              # Random numbers
        }
        self.auth_service = auth_service
    
    def _fetch_numbers(self, number_id: str) -> List[int]:
        """
        Fetch numbers from the test server based on the number ID.
        
        Args:
            number_id: 'p' for prime, 'f' for Fibonacci, 'e' for even, 'r' for random
        
        Returns:
            List of numbers returned by the API
        """
        if number_id not in self.number_types:
            raise ValueError(f"Invalid number ID: {number_id}. Must be one of {list(self.number_types.keys())}")
        
        # Get the endpoint based on number_id
        endpoint = self.number_types[number_id]
        url = f"{self.base_url}/{endpoint}"
        
        # Get authentication token
        token = self.auth_service.get_token()
        
        # Set headers with token
        headers = {"Authorization": f"Bearer {token}"}
        
        try:
            # Set timeout to 500ms (0.5 seconds) as per requirement
            response = requests.get(url, headers=headers, timeout=0.5)
            
            if response.status_code == 200:
                data = response.json()
                return data.get("numbers", [])
            else:
                logger.error(f"Error fetching numbers: {response.status_code} - {response.text}")
                return []
        except requests.exceptions.Timeout:
            logger.warning(f"Request to {url} timed out")
            return []
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching numbers: {str(e)}")
            return []
    
    def calculate_average(self, number_id: str) -> Dict[str, Any]:
        """
        Calculate the average of numbers based on the number ID.
        
        Args:
            number_id: 'p' for prime, 'f' for Fibonacci, 'e' for even, 'r' for random
        
        Returns:
            Dictionary with previous window state, current window state, 
            numbers fetched, and average
        """
        # Store the previous state of the window
        prev_state = self.numbers_window.copy()
        
        # Fetch numbers from the test server
        fetched_numbers = self._fetch_numbers(number_id)
        
        # Update the window with unique numbers
        for num in fetched_numbers:
            # Only add numbers that aren't already in the window
            if num not in self.numbers_window:
                # If window is full, remove the oldest number (first in the list)
                if len(self.numbers_window) >= self.window_size:
                    self.numbers_window.pop(0)  # Remove oldest element (first in list)
                # Add the new number
                self.numbers_window.append(num)
        
        # Calculate average of the current window
        current_state = self.numbers_window.copy()
        avg = sum(current_state) / len(current_state) if current_state else 0
        
        # Format the response as per requirement
        response = {
            "windowPrevState": prev_state,
            "windowCurrState": current_state,
            "numbers": fetched_numbers,
            "avg": round(avg, 2)  # Round to 2 decimal places
        }
        
        return response