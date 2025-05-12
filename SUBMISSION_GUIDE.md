# GitHub Submission Guide

This guide will help you prepare this project for submission to GitHub.

## Step 1: Download the code

Download all files from this project to your local machine.

## Step 2: Create your GitHub repository

1. Create a new repository on GitHub with your roll number as the name
2. Make sure it's a public repository
3. Do not include your name or any mention of Affordmed in the repository name, README, or commit messages

## Step 3: Generate API output examples

1. Run the screenshot generator script:
   ```
   python create_screenshots.py
   ```
2. This will create example API outputs in the `screenshots` folders of both microservices

## Step 4: Create API screenshots

For your GitHub submission, you need screenshots of API responses. Since you mentioned you don't have Postman installed, you have several options:

1. **Text files**: The generator script has created example text files in the `screenshots` folders. You can take screenshots of these files.

2. **HTML API Testers**: Open the HTML testers in your browser and take screenshots of the responses:
   - `Average-Calculator-Microservice/api_tester.html`
   - `Stock-Price-Aggregation-Microservice/api_tester.html`

3. **Format in an editor**: Copy the content from the example text files and format them nicely in your preferred editor, then take screenshots.

## Step 5: Prepare your commit

1. Add all the files to your local repository
2. Commit with a message that doesn't include your name or any mention of Affordmed
3. Push to your GitHub repository

## Step 6: Verify your repository

Make sure your GitHub repository contains:

- README.md in the root directory
- Two folders for the two microservices
- All the code files in both folders
- Screenshot images in the screenshots directories
- No mention of your name or Affordmed anywhere in the repository

## Required Screenshots

For the **Average Calculator Microservice**:
1. Health check endpoint (`/`)
2. Prime numbers endpoint (`/numbers/p`)
3. Fibonacci numbers endpoint (`/numbers/f`)
4. Even numbers endpoint (`/numbers/e`) 
5. Random numbers endpoint (`/numbers/r`)

For the **Stock Price Aggregation Microservice**:
1. Health check endpoint (`/`)
2. List stocks endpoint (`/stocks`)
3. Stock average price endpoint (`/stocks/AAPL?minutes=30&aggregation=average`)
4. Stock correlation endpoint (`/stocks/correlation?minutes=30&ticker=AAPL&ticker=MSFT`)