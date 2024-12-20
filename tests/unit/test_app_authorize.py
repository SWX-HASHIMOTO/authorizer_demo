import json
import pytest

from authorizer.app import lambda_handler
from unittest.mock import MagicMock

TOKEN = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRkYVFKMzk1OHZZQkN5cVVJQVBIOSJ9.eyJpc3MiOiJodHRwczovL2Rldi1xeTVnaGJ6YTdrend4cHVjLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJEZEYxQXN2VU1uaUZXazB5czhoa1RMNzV3MUpUZUVCbkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9oY3lja3Ztd20yLmV4ZWN1dGUtYXBpLmFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20vIiwiaWF0IjoxNzM0Njc5NjA4LCJleHAiOjE3MzQ3NjYwMDgsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6IkRkRjFBc3ZVTW5pRldrMHlzOGhrVEw3NXcxSlRlRUJuIn0.woRn3nZeUxzvz_LT3PS1lDsGQzgBiV-xMfp3Y5JvGbWTDDeY42dyLBGYm-N6mdmHE2TF2oW9k-wsfqi5gIKUqfLaxbzt9dso3MeRoUPQOsxylo2rvk3E9b9tZd3dhkFc2o2yPrtKgdc7vkLu3CNh7sHtKSQ7AsAtJ8B5NA3YFO9qdaQGaWabHsVF7-PAmO82-G_DTatff53Q_sxYrwVgt1I55BDdtfKh2sv0a1BJuZ9l6gasw1S0wOEsS8NmXC_1fNponKdJaLeHKSZJxkd7E4gGEtZdEARUtbZ_kp2k53VpfCV5c-WlESfRIufwYpOw_6A6dI0RtaagUwtBj6zziA"


@pytest.fixture
def test_event():
    return {
        "type": "TOKEN",
        "authorizationToken": TOKEN,
        "methodArn": "",
    }


@pytest.fixture
def lambda_context():
    """Create a mock for the Lambda context."""
    context = MagicMock()
    yield context


@pytest.mark.success
def test_lambda_handler_success(test_event):

    # Test the Lambda handler.
    response = lambda_handler(test_event, lambda_context)

    # Normal system testing
    assert response


@pytest.mark.exception
def test_lambda_handler_exception(lambda_context):

    # Anticipated messages
    ERROR_MESSAGE = "Unauthorized"

    # Test the authenticate.
    with pytest.raises(Exception) as e:
        # Test the Lambda handler.
        lambda_handler("", lambda_context)

    # Assert Exception.
    assert str(e.value) == ERROR_MESSAGE
