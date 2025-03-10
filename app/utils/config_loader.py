import yaml
import os
from app.core.logger import logger

def load_credentials():
    """Load credentials from credentials.yaml file."""
    try:
        # Get the path to the credentials file
        credentials_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'credentials.yaml')
        
        # Check if the file exists
        if not os.path.exists(credentials_path):
            logger.warning("Credentials file not found. Using default credentials.")
            return {"auth": {"username": "admin", "password": "password"}}
        
        # Load the credentials
        with open(credentials_path, 'r') as file:
            credentials = yaml.safe_load(file)
            
        return credentials
    except Exception as e:
        logger.error(f"Error loading credentials: {str(e)}")
        # Return default credentials if there's an error
        return {"auth": {"username": "admin", "password": "password"}} 