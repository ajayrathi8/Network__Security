import sys
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class NetworkSecurityException(Exception):
    """
    Base exception class for all Network Security related errors.
    All custom exceptions in this module inherit from this class.
    """
    
    def __init__(
        self,
        error_message: str,
        error_code: Optional[int] = None,
        error_details: Optional[dict] = None
    ):
        """
        Initialize NetworkSecurityException
        
        Args:
            error_message: Description of the error
            error_code: Optional error code for categorization
            error_details: Optional dictionary with additional error details
        """
        self.error_message = error_message
        self.error_code = error_code
        self.error_details = error_details or {}
        
        super().__init__(self.error_message)
        
        # Log the exception
        logger.error(
            f"NetworkSecurityException: {error_message} (Code: {error_code})",
            extra={"error_details": self.error_details}
        )
    
    def __str__(self) -> str:
        return f"NetworkSecurityException: {self.error_message}"
    
    def get_error_details(self) -> dict:
        """Return detailed error information"""
        return {
            "error_message": self.error_message,
            "error_code": self.error_code,
            "error_details": self.error_details
        }


class DataIngestionException(NetworkSecurityException):
    """Exception raised during data ingestion operations"""
    pass


class DataValidationException(NetworkSecurityException):
    """Exception raised when data validation fails"""
    pass


class DataTransformationException(NetworkSecurityException):
    """Exception raised during data transformation"""
    pass


class ModelTrainingException(NetworkSecurityException):
    """Exception raised during model training"""
    pass


class ModelPredictionException(NetworkSecurityException):
    """Exception raised during model prediction"""
    pass


class FeatureExtractionException(NetworkSecurityException):
    """Exception raised during feature extraction"""
    pass


class DatabaseException(NetworkSecurityException):
    """Exception raised for database-related operations"""
    pass


class APIException(NetworkSecurityException):
    """Exception raised for API-related operations"""
    pass


class ConfigurationException(NetworkSecurityException):
    """Exception raised for configuration errors"""
    pass


class FileOperationException(NetworkSecurityException):
    """Exception raised during file operations"""
    pass


class AuthenticationException(NetworkSecurityException):
    """Exception raised for authentication failures"""
    pass


class AuthorizationException(NetworkSecurityException):
    """Exception raised for authorization failures"""
    pass


class ExternalServiceException(NetworkSecurityException):
    """Exception raised when external service calls fail"""
    pass


def handle_exception(
    exc: Exception,
    context: Optional[str] = None,
    raise_exception: bool = True
) -> Optional[dict]:
    """
    Utility function to handle and log exceptions uniformly
    
    Args:
        exc: The exception to handle
        context: Optional context string describing where the exception occurred
        raise_exception: Whether to re-raise the exception after handling
        
    Returns:
        Dictionary with error details if raise_exception is False
    """
    error_info = {
        "error_type": type(exc).__name__,
        "error_message": str(exc),
        "context": context or "Unknown context"
    }
    
    logger.error(
        f"Exception in {context}: {type(exc).__name__} - {str(exc)}",
        exc_info=True
    )
    
    if raise_exception:
        if isinstance(exc, NetworkSecurityException):
            raise exc
        else:
            raise NetworkSecurityException(
                error_message=str(exc),
                error_details=error_info
            )
    
    return error_info



# define __all__ for explicit exports

