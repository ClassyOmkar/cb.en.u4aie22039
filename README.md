# Microservices Implementation

This repository contains two microservices:

1. **Average Calculator Microservice**: Calculates the average of numbers fetched from an external API.
2. **Stock Price Aggregation Microservice**: Provides stock price aggregation and correlation analysis.

## Project Structure

```
.
├── Average-Calculator-Microservice/
│   ├── auth_service.py       # Authentication service
│   ├── average_calculator.py # Calculator implementation
│   ├── app.py               # Flask application setup
│   ├── main.py              # Entry point
│   ├── requirements.txt     # Dependencies
│   └── README.md            # Documentation
│
└── Stock-Price-Aggregation-Microservice/
    ├── auth_service.py      # Authentication service
    ├── stock_service.py     # Stock service implementation
    ├── app.py               # Flask application setup
    ├── main.py              # Entry point
    ├── requirements.txt     # Dependencies
    └── README.md            # Documentation
```

## Getting Started

### Average Calculator Microservice

1. Navigate to the Average Calculator directory:
   ```
   cd Average-Calculator-Microservice
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the service:
   ```
   python main.py
   ```

4. Access the service at http://localhost:9876

### Stock Price Aggregation Microservice

1. Navigate to the Stock Price Aggregation directory:
   ```
   cd Stock-Price-Aggregation-Microservice
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the service:
   ```
   python main.py
   ```

4. Access the service at http://localhost:9877

## Testing

Both microservices can be tested using API clients like Postman or Insomnia. Refer to the individual service README files for specific endpoint documentation and example responses.