import time
import logging
import requests
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class AuthService:
    def __init__(self):
        self.base_url = "http://20.244.56.144/evaluation-service"
        self.register_url = f"{self.base_url}/register"
        self.auth_url = f"{self.base_url}/auth"
        self.token = None
        self.token_expiry = None
        
        # Full credentials needed for auth
        self.credentials = None
        
    def register(self, name: str, email: str, roll_no: str, access_code: str, 
                mobile_no: str, github_username: str, college_name: str) -> Dict[str, str]:
        """
        Register with the evaluation service to get client credentials.
        This should be called only once as mentioned in the API docs.
        """
        payload = {
            "name": name,
            "email": email,
            "rollNo": roll_no,
            "accessCode": access_code,
            "mobileNo": mobile_no,
            "githubUsername": github_username,
            "collegeName": college_name
        }
        
        response = requests.post(self.register_url, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            # Store all registration info plus the returned client credentials
            self.credentials = payload.copy()
            self.credentials["clientID"] = data["clientID"]
            self.credentials["clientSecret"] = data["clientSecret"]
            logger.info("Registration successful")
            return data
        else:
            logger.error(f"Registration failed: {response.text}")
            raise Exception(f"Registration failed: {response.text}")
    
    def get_token(self) -> str:
        """
        Get an authentication token from the evaluation service.
        If a token already exists and is valid, return it.
        Otherwise, request a new token.
        """
        # Check if token exists and is valid
        current_time = int(time.time())
        if self.token and self.token_expiry and current_time < self.token_expiry - 300:  # 5 minutes buffer
            return self.token
        
        # Request a new token
        if not self.credentials:
            raise Exception("No credentials found. Please set credentials first.")
        
        # Send all credentials to auth endpoint
        try:
            response = requests.post(self.auth_url, json=self.credentials)
            data = response.json()
            
            if "access_token" in data:
                self.token = data["access_token"]
                # Parse expiry time or set default (30 minutes)
                if "expires_in" in data:
                    self.token_expiry = current_time + int(data["expires_in"])
                else:
                    self.token_expiry = current_time + 1800  # 30 minutes default
                
                logger.info("Authentication successful")
                return self.token
            else:
                logger.error(f"Authentication response missing access_token: {data}")
                raise Exception(f"Authentication failed: {response.text}")
        except Exception as e:
            logger.error(f"Authentication error: {str(e)}")
            raise
    
    def set_credentials(self, credentials: Dict[str, str]) -> None:
        """
        Set credentials manually.
        """
        self.credentials = credentials
        logger.info("Credentials set manually")