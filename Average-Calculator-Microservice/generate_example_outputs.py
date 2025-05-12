"""
Generate example outputs for Average Calculator API.
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
        "service": "Average Calculator"
    },
    "numbers_p": {
        "windowPrevState": [53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
        "windowCurrState": [5, 8, 13, 21, 34, 55, 144, 233, 377, 610],
        "numbers": [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610],
        "avg": 150.0
    },
    "numbers_f": {
        "windowPrevState": [5, 8, 13, 21, 34, 55, 144, 233, 377, 610],
        "windowCurrState": [5, 8, 13, 21, 34, 55, 144, 233, 377, 610],
        "numbers": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610],
        "avg": 150.0
    },
    "numbers_e": {
        "windowPrevState": [5, 8, 13, 21, 34, 55, 144, 233, 377, 610],
        "windowCurrState": [8, 10, 12, 14, 16, 18, 20, 22, 24, 26],
        "numbers": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
        "avg": 17.0
    },
    "numbers_r": {
        "windowPrevState": [8, 10, 12, 14, 16, 18, 20, 22, 24, 26],
        "windowCurrState": [15, 12, 2, 19, 25, 7, 4, 24, 17, 27],
        "numbers": [6, 15, 12, 2, 19, 25, 7, 4, 24, 17, 27],
        "avg": 15.2
    }
}

# Generate example outputs for each endpoint
def generate_example_output(endpoint_name, response_data, status=200):
    # Create a mock API request/response
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Generate random response time (realistic but variable)
    response_time = round(random.uniform(0.05, 0.3), 3)
    
    # Format the output as if it was a real API response
    output = f"""REQUEST: GET http://localhost:9876{endpoint_name}
TIME: {now}
STATUS: {status}
RESPONSE TIME: {response_time} seconds

RESPONSE BODY:
{json.dumps(response_data, indent=4)}
"""
    
    # Save to a file
    filename = f"screenshots/example_{endpoint_name.replace('/', '_')}.txt"
    if endpoint_name == "/":
        filename = "screenshots/example_health.txt"
    
    with open(filename, "w") as f:
        f.write(output)
    
    print(f"Generated example output for {endpoint_name}")

# Generate examples for all endpoints
generate_example_output("/", EXAMPLE_RESPONSES["health"])
generate_example_output("/numbers/p", EXAMPLE_RESPONSES["numbers_p"])
generate_example_output("/numbers/f", EXAMPLE_RESPONSES["numbers_f"])
generate_example_output("/numbers/e", EXAMPLE_RESPONSES["numbers_e"])
generate_example_output("/numbers/r", EXAMPLE_RESPONSES["numbers_r"])

print("\nExample outputs generated successfully in the 'screenshots' directory.")
print("You can use these as references for creating your API response screenshots.")
print("Remember: The actual submission should use real screenshots from tools like Postman or Insomnia.")