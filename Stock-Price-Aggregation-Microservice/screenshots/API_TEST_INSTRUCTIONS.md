# API Testing Instructions

This folder is where you should place screenshots of API responses from Postman, Insomnia, or another API testing tool.

## Running the API Tests

1. **Start the server**: 
   ```
   cd Stock-Price-Aggregation-Microservice
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
     - `GET http://localhost:9877/`
     - `GET http://localhost:9877/stocks`
     - `GET http://localhost:9877/stocks/AAPL?minutes=30&aggregation=average`
     - `GET http://localhost:9877/stocks/correlation?minutes=30&ticker=AAPL&ticker=MSFT`
   - Take screenshots of the requests and responses

## Required Screenshots

For your submission, you should have screenshots of API responses for:

1. Health check endpoint (`/`)
2. List stocks endpoint (`/stocks`)
3. Stock average price endpoint (`/stocks/AAPL?minutes=30&aggregation=average`)
4. Stock correlation endpoint (`/stocks/correlation?minutes=30&ticker=AAPL&ticker=MSFT`)

Each screenshot should clearly show:
- The request URL and method
- The response status code
- The response time
- The response body

## Example Response Format

```
REQUEST: GET http://localhost:9877/stocks
TIME: 2023-07-15 14:35:10
STATUS: 200
RESPONSE TIME: 0.156 seconds

RESPONSE BODY:
{
    "stocks": {
        "Apple Inc.": "AAPL",
        "Microsoft Corporation": "MSFT",
        "Amazon.com, Inc.": "AMZN",
        "Alphabet Inc.": "GOOGL",
        "Meta Platforms, Inc.": "META"
    }
}
```