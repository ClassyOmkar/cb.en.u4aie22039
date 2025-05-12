"""
Script to test the Stock Price Aggregation API and generate example outputs.
This can be used to capture the API responses for documentation purposes.
"""

import requests
import json
import time
from datetime import datetime

# Configuration
BASE_URL = "http://localhost:9877"
ENDPOINTS = {
    "health": "/",
    "stocks_list": "/stocks",
    "apple_average": "/stocks/AAPL?minutes=30&aggregation=average",
    "stocks_correlation": "/stocks/correlation?minutes=30&ticker=AAPL&ticker=MSFT"
}

def format_response(url, response, elapsed_time):
    """Format a response for display in a nice, readable way."""
    print("=" * 80)
    print(f"REQUEST: GET {url}")
    print(f"TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 80)
    print(f"STATUS: {response.status_code}")
    print(f"RESPONSE TIME: {elapsed_time:.3f} seconds")
    print("-" * 80)
    print("HEADERS:")
    for key, value in response.headers.items():
        print(f"    {key}: {value}")
    print("-" * 80)
    
    # Print formatted JSON response if content exists and is JSON
    try:
        if response.text:
            json_data = json.loads(response.text)
            formatted_json = json.dumps(json_data, indent=4)
            print("RESPONSE BODY:")
            print(formatted_json)
    except json.JSONDecodeError:
        print("RESPONSE BODY:")
        print(response.text)
    print("=" * 80)
    print("\n")

def test_endpoint(endpoint_name, endpoint_path):
    """Test an endpoint and format the response."""
    url = f"{BASE_URL}{endpoint_path}"
    print(f"Testing endpoint: {endpoint_name} - {url}")
    
    try:
        start_time = time.time()
        response = requests.get(url)
        elapsed_time = time.time() - start_time
        
        format_response(url, response, elapsed_time)
        
        # Also save to a text file for later reference
        with open(f"screenshots/{endpoint_name}_response.txt", "w") as f:
            f.write(f"REQUEST: GET {url}\n")
            f.write(f"TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"STATUS: {response.status_code}\n")
            f.write(f"RESPONSE TIME: {elapsed_time:.3f} seconds\n\n")
            
            # Write JSON response if available
            try:
                if response.text:
                    json_data = json.loads(response.text)
                    formatted_json = json.dumps(json_data, indent=4)
                    f.write("RESPONSE BODY:\n")
                    f.write(formatted_json)
            except json.JSONDecodeError:
                f.write("RESPONSE BODY:\n")
                f.write(response.text)
                
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error testing {endpoint_name}: {str(e)}")
        return False

def main():
    """Test all endpoints of the Stock Price Aggregation API."""
    print("TESTING STOCK PRICE AGGREGATION API")
    print("Make sure the server is running at", BASE_URL)
    print("\n")
    
    # Create screenshots directory if it doesn't exist
    import os
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    # Test all endpoints
    for name, path in ENDPOINTS.items():
        test_endpoint(name, path)

if __name__ == "__main__":
    main()