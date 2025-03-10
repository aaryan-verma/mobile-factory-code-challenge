from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from app.utils.config_loader import load_credentials
from app.core.logger import logger

security = HTTPBasic(auto_error=False)  # Set auto_error to False to handle missing auth ourselves

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    # Check if credentials were provided
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    # Load credentials from file
    config = load_credentials()
    correct_username = config["auth"]["username"]
    correct_password = config["auth"]["password"]
    
    logger.debug(f"Authenticating user: {credentials.username}")
    
    # Use secrets.compare_digest to prevent timing attacks
    is_username_correct = secrets.compare_digest(credentials.username, correct_username)
    is_password_correct = secrets.compare_digest(credentials.password, correct_password)
    
    # Check if credentials are valid
    if not (is_username_correct and is_password_correct):
        logger.warning(f"Failed authentication attempt for user: {credentials.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    logger.info(f"User authenticated successfully: {credentials.username}")
    return credentials 