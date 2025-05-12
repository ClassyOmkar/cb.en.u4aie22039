"""
Generate example outputs for Stock Price Aggregation API.
This script creates realistic example responses that mimic the API behavior,
which can be used for documentation and screenshots.
"""

import json
import os
import random
from datetime import datetime

# Create screenshots directory if it doesn't exist
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Example data
EXAMPLE_RESPONSES = {
    "health": {
        "status": "healthy", 
        "service": "Stock Price Aggregation"
    },
    "stocks": {
        "stocks": {
            "Advanced Micro Devices, Inc.": "AMD",
            "Alphabet Inc. Class A": "GOOGL",
            "Alphabet Inc. Class C": "GOOG",
            "Amazon.com, Inc.": "AMZN",
            "Amgen Inc.": "AMGN",
            "Apple Inc.": "AAPL",
            "Cisco Systems, Inc.": "CSCO",
            "Meta Platforms Inc.": "META",
            "Microsoft Corporation": "MSFT",
            "NVIDIA Corporation": "NVDA"
        }
    },
    "stock_average": {
        "averageStockPrice": 746.1452674999999,
        "priceHistory": [
            {
                "price": 751.24,
                "timestamp": "2023-07-15T13:30:00Z"
            },
            {
                "price": 745.67,
                "timestamp": "2023-07-15T13:45:00Z"
            },
            {
                "price": 747.89,
                "timestamp": "2023-07-15T14:00:00Z"
            },
            {
                "price": 739.78,
                "timestamp": "2023-07-15T14:15:00Z"
            }
        ]
    },
    "stock_correlation": {
        "correlation": 0.8724,
        "stocks": {
            "AAPL": {
                "averageStockPrice": 746.1452674999999,
                "priceHistory": [
                    {
                        "price": 751.24,
                        "timestamp": "2023-07-15T13:30:00Z"
                    },
                    {
                        "price": 745.67,
                        "timestamp": "2023-07-15T13:45:00Z"
                    },
                    {
                        "price": 747.89,
                        "timestamp": "2023-07-15T14:00:00Z"
                    },
                    {
                        "price": 739.78,
                        "timestamp": "2023-07-15T14:15:00Z"
                    }
                ]
            },
            "MSFT": {
                "averageStockPrice": 325.7625,
                "priceHistory": [
                    {
                        "price": 329.21,
                        "timestamp": "2023-07-15T13:30:00Z"
                    },
                    {
                        "price": 326.45,
                        "timestamp": "2023-07-15T13:45:00Z"
                    },
                    {
                        "price": 327.12,
                        "timestamp": "2023-07-15T14:00:00Z"
                    },
                    {
                        "price": 320.27,
                        "timestamp": "2023-07-15T14:15:00Z"
                    }
                ]
            }
        }
    }
}

# Generate example outputs for each endpoint
def generate_example_output(endpoint_name, endpoint_path, response_data, status=200):
    # Create a mock API request/response
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Generate random response time (realistic but variable)
    response_time = round(random.uniform(0.05, 0.3), 3)
    
    # Format the output as if it was a real API response
    output = f"""REQUEST: GET http://localhost:9877{endpoint_path}
TIME: {now}
STATUS: {status}
RESPONSE TIME: {response_time} seconds

RESPONSE BODY:
{json.dumps(response_data, indent=4)}
"""
    
    # Save to a file
    filename = f"screenshots/example_{endpoint_name}.txt"
    
    with open(filename, "w") as f:
        f.write(output)
    
    print(f"Generated example output for {endpoint_name}")

# Generate examples for all endpoints
generate_example_output("health", "/", EXAMPLE_RESPONSES["health"])
generate_example_output("stocks", "/stocks", EXAMPLE_RESPONSES["stocks"])
generate_example_output("stock_average", "/stocks/AAPL?minutes=30&aggregation=average", EXAMPLE_RESPONSES["stock_average"])
generate_example_output("stock_correlation", "/stocks/correlation?minutes=30&ticker=AAPL&ticker=MSFT", EXAMPLE_RESPONSES["stock_correlation"])

print("\nExample outputs generated successfully in the 'screenshots' directory.")
print("You can use these as references for creating your API response screenshots.")
print("Remember: The actual submission should use real screenshots from tools like Postman or Insomnia.")