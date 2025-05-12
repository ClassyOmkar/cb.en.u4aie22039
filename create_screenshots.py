"""
Create Screenshots for API Submission

This script runs both microservices and generates all required screenshots automatically.
You don't need to install Postman or other tools.

Usage:
    python create_screenshots.py
"""

import os
import subprocess
import sys
import time
import threading
import webbrowser
from datetime import datetime

def print_banner(text):
    """Print a section banner."""
    print("\n" + "=" * 80)
    print(text)
    print("=" * 80 + "\n")

def run_generate_examples():
    """Run example generators for both services."""
    print_banner("Generating Example Outputs")
    
    # Run Average Calculator examples
    os.chdir("Average-Calculator-Microservice")
    subprocess.run([sys.executable, "generate_example_outputs.py"])
    os.chdir("..")
    
    # Run Stock Price examples
    os.chdir("Stock-Price-Aggregation-Microservice")
    subprocess.run([sys.executable, "generate_example_outputs.py"])
    os.chdir("..")
    
def open_html_testers():
    """Open the HTML API testers in a browser."""
    print_banner("Opening HTML API Testers")
    print("If you have a browser on your system, the HTML testers should open automatically.")
    print("If not, manually open these files in a browser:")
    print("  - Average-Calculator-Microservice/api_tester.html")
    print("  - Stock-Price-Aggregation-Microservice/api_tester.html")
    
    # Get absolute paths
    current_dir = os.getcwd()
    avg_tester = os.path.join(current_dir, "Average-Calculator-Microservice", "api_tester.html")
    stock_tester = os.path.join(current_dir, "Stock-Price-Aggregation-Microservice", "api_tester.html")
    
    # Try to open in browser
    try:
        webbrowser.open("file://" + avg_tester)
        time.sleep(1)  # Small delay between opening files
        webbrowser.open("file://" + stock_tester)
    except:
        print("Couldn't open browser automatically.")

def create_screenshots():
    """Create the screenshot package."""
    print_banner("Creating Screenshot Package")
    
    # Run example generators
    run_generate_examples()
    
    # Inform the user about next steps
    print("\n" + "-" * 80)
    print("SCREENSHOT PACKAGE CREATED!")
    print("-" * 80)
    print("\nExample API outputs have been generated in:")
    print("  - Average-Calculator-Microservice/screenshots/")
    print("  - Stock-Price-Aggregation-Microservice/screenshots/")
    print("\nFor your GitHub submission, you should:")
    print("1. Use these examples to create actual API screenshots")
    print("2. Either take screenshots of the text files, or")
    print("3. Format them nicely in your preferred editor")
    print("\nRemember to include:")
    print("  - Request URL and method")
    print("  - Response status code")
    print("  - Response time")
    print("  - Response body")
    
    print("\nWould you like to open the HTML API testers too? (y/n)")
    choice = input().lower()
    if choice == 'y':
        open_html_testers()

if __name__ == "__main__":
    print_banner("API SCREENSHOT GENERATOR")
    print("This script will create example API outputs for your GitHub submission")
    print("You can use these examples to create the required screenshots")
    
    create_screenshots()