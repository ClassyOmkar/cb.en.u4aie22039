# Stock Price Aggregation Microservice

This microservice fetches stock price data from an external API and provides endpoints for calculating average stock prices and correlation between two stocks over a specified time window.

## Features

- Lists all available stocks on the exchange
- Calculates the average price of a stock over a specified time window
- Calculates the correlation between two stocks' price movements
- Implements caching to minimize API calls
- Handles different API response formats
- Authenticates with external API using OAuth2

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The service is pre-configured to communicate with the evaluation service API. You can modify the following in `main.py`:

- `credentials`: Update with your own API credentials
- `port`: Change the port number (default: 9877)

## Usage

Start the server:

```bash
python main.py
```

This will start the service on http://localhost:9877.

## API Endpoints

### GET /stocks

Returns a list of all available stocks on the exchange.

Example Response:
```json
{
   "stocks": {
      "Apple Inc.": "AAPL",
      "Microsoft Corporation": "MSFT",
      "Amazon.com, Inc.": "AMZN"
   }
}
```

### GET /stocks/{ticker}?minutes={m}&aggregation=average

Calculates the average price of a stock over the specified time window.

Parameters:
- `ticker`: Stock ticker symbol (e.g., AAPL, MSFT)
- `minutes`: Time window in minutes (required)
- `aggregation`: Type of aggregation (only 'average' is currently supported)

Example Response:
```json
{
   "averageStockPrice": 156.78,
   "priceHistory": [
      {"price": 155.23, "timestamp": "2023-07-15T14:30:00Z"},
      {"price": 156.45, "timestamp": "2023-07-15T14:35:00Z"},
      {"price": 158.67, "timestamp": "2023-07-15T14:40:00Z"}
   ]
}
```

### GET /stocks/correlation?minutes={m}&ticker={ticker1}&ticker={ticker2}

Calculates the correlation between two stocks' price movements over the specified time window.

Parameters:
- `minutes`: Time window in minutes (required)
- `ticker`: Stock ticker symbols (must be specified exactly twice)

Example Response:
```json
{
   "correlation": 0.8532,
   "stocks": {
      "AAPL": {
         "averageStockPrice": 156.78,
         "priceHistory": [...]
      },
      "MSFT": {
         "averageStockPrice": 325.42,
         "priceHistory": [...]
      }
   }
}
```

### GET /

Health check endpoint.

Example Response:
```json
{
   "status": "healthy", 
   "service": "Stock Price Aggregation"
}
```

## Testing with Postman/Insomnia

You can test the API using tools like Postman or Insomnia:

1. Send a GET request to `http://localhost:9877/stocks` to get all available stocks
2. Send a GET request to `http://localhost:9877/stocks/AAPL?minutes=30&aggregation=average` to get the average price of Apple stock over the last 30 minutes
3. Send a GET request to `http://localhost:9877/stocks/correlation?minutes=30&ticker=AAPL&ticker=MSFT` to get the correlation between Apple and Microsoft stocks

## Screenshot

(Screenshots of API responses would be placed here)