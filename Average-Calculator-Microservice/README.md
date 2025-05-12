# Average Calculator Microservice

This microservice calculates the average of numbers fetched from an external API. It maintains a window of unique numbers and responds with the state before and after the API call.

## Features

- Fetches prime, Fibonacci, even, or random numbers from an external API
- Maintains a configurable window size of unique numbers (default: 10)
- Returns detailed information including previous window state, current window state, fetched numbers, and the calculated average
- Handles API timeouts and errors gracefully
- Ensures uniqueness of numbers in the window
- Replaces oldest numbers when the window is full
- Authenticates with external API using OAuth2

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The service is pre-configured to use a window size of 10 and communicate with the evaluation service API. You can modify the following in `main.py`:

- `credentials`: Update with your own API credentials
- `window_size`: Change the size of the number window (default: 10)
- `port`: Change the port number (default: 9876)

## Usage

Start the server:

```bash
python main.py
```

This will start the service on http://localhost:9876.

## API Endpoints

### GET /numbers/{number_id}

Fetches numbers from the server based on the number ID and calculates their average.

Parameters:
- `number_id`: Type of numbers to fetch ('p', 'f', 'e', or 'r')
  - 'p': Prime numbers
  - 'f': Fibonacci numbers
  - 'e': Even numbers
  - 'r': Random numbers

Example Response:
```json
{
   "windowPrevState": [2, 4, 6, 8],
   "windowCurrState": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
   "numbers": [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
   "avg": 11.0
}
```

### GET /

Health check endpoint.

Example Response:
```json
{
   "status": "healthy", 
   "service": "Average Calculator"
}
```

## Testing with Postman/Insomnia

You can test the API using tools like Postman or Insomnia:

1. Send a GET request to `http://localhost:9876/numbers/p` for prime numbers
2. Send a GET request to `http://localhost:9876/numbers/f` for Fibonacci numbers
3. Send a GET request to `http://localhost:9876/numbers/e` for even numbers
4. Send a GET request to `http://localhost:9876/numbers/r` for random numbers

## Screenshot

(Screenshots of API responses would be placed here)