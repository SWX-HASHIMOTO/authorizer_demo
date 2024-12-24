import os
import pytest

from authorizer.app import lambda_handler
from authorizer.token_utils import TokenUtils
from unittest.mock import MagicMock

# Get value from environment variable
AUDIENCE = os.getenv("AUDIENCE")
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


@pytest.fixture
def access_token():
    token_utils = TokenUtils(CLIENT_ID, CLIENT_SECRET, AUDIENCE, AUTH0_DOMAIN)
    response = token_utils.get_token()
    return f"{response["token_type"]} {response["access_token"]}"


@pytest.fixture
def test_event(access_token):
    return {
        "type": "TOKEN",
        "authorizationToken": access_token,
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
