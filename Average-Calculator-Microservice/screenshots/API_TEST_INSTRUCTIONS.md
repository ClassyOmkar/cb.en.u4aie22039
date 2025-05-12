# API Testing Instructions

This folder is where you should place screenshots of API responses from Postman, Insomnia, or another API testing tool.

## Running the API Tests

1. **Start the server**: 
   ```
   cd Average-Calculator-Microservice
   python main.py
   ```

2. **Option 1 - Use the HTML tester**:
   - Open `api_tester.html` in your browser
   - Click "Test Endpoint" for each endpoint
   - Take screenshots of the responses

3. **Option 2 - Use the Python script**:
   - Run the test script: `python test_api.py`
   - Check the console output
   - Test results will also be saved in text files in this directory

4. **Option 3 - Use Postman/Insomnia/curl**:
   - Make requests to the following endpoints:
     - `GET http://localhost:9876/`
     - `GET http://localhost:9876/numbers/p`
     - `GET http://localhost:9876/numbers/f`
     - `GET http://localhost:9876/numbers/e`
     - `GET http://localhost:9876/numbers/r`
   - Take screenshots of the requests and responses

## Required Screenshots

For your submission, you should have screenshots of API responses for:

1. Health check endpoint (`/`)
2. Prime numbers endpoint (`/numbers/p`)
3. Fibonacci numbers endpoint (`/numbers/f`)
4. Even numbers endpoint (`/numbers/e`)
5. Random numbers endpoint (`/numbers/r`)

Each screenshot should clearly show:
- The request URL and method
- The response status code
- The response time
- The response body

## Example Response Format

```
REQUEST: GET http://localhost:9876/numbers/p
TIME: 2023-07-15 14:30:25
STATUS: 200
RESPONSE TIME: 0.123 seconds

RESPONSE BODY:
{
    "windowPrevState": [],
    "windowCurrState": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    "numbers": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
    "avg": 12.9
}
```