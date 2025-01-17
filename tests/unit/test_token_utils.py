import http.client
import os
import json
import pytest
from unittest.mock import patch

from authorizer.token_utils import TokenUtils

from unittest.mock import MagicMock

AUDIENCE = os.getenv("AUDIENCE")
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


@pytest.fixture
def token_utils():
    """
    TokenUtils fixture
    """
    token_utils = TokenUtils()
    yield token_utils


@pytest.fixture
def token_utils_ng():
    """
    TokenUtils fixture for Exception
    Set broken domains.
    """
    os.environ["AWS_LAMBDA_FUNCTION_NAME"] = "authorizer_demo"
    token_utils = TokenUtils()
    yield token_utils


@pytest.fixture
def mock_conn_instance():
    # Mock object settings.
    mock_conn_instance = MagicMock()
    yield mock_conn_instance


@pytest.fixture
def mock_response():
    # Mock object settings.
    mock_response = MagicMock()
    yield mock_response


@pytest.fixture
def payload_dic():
    return {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": AUDIENCE,
        "grant_type": "client_credentials",
    }


@pytest.mark.success
@patch("authorizer.token_utils.http.client.HTTPSConnection")
def test_token_utils_success(
    mock_https_conn,
    payload_dic,
    token_utils,
    mock_conn_instance,
    mock_response,
):

    # Mock object settings.
    mock_https_conn.return_value = mock_conn_instance

    # Set mock response.
    mock_response.read.return_value = json.dumps({"access_token": "test_token", "token_type": "test_type"}).encode(
        "utf-8"
    )
    mock_response.status = 200

    # Set response data in Mock.
    mock_conn_instance.getresponse.return_value = mock_response

    # Execute Function
    result = token_utils.get_token()

    # Verify results.
    assert result == {"access_token": "test_token", "token_type": "test_type"}

    # Confirmation of HTTPS request. (Not actually sent)
    mock_https_conn.assert_called_once_with(AUTH0_DOMAIN)
    mock_conn_instance.request.assert_called_once_with(
        "POST",
        "/oauth/token",
        json.dumps(payload_dic),
        {"content-type": "application/json"},
    )
    mock_conn_instance.getresponse.assert_called_once()


@pytest.mark.exception
@patch("authorizer.token_utils.http.client.HTTPSConnection")
def test_token_utils_httpexception(
    mock_https_conn,
    token_utils,
    mock_conn_instance,
):

    # Mock object settings.
    mock_https_conn.return_value = mock_conn_instance

    # Set HTTPException in Mock.
    mock_conn_instance.getresponse.side_effect = http.client.HTTPException("Test HTTP error")

    response = token_utils.get_token()

    body = json.loads(response["body"])

    # Assert HTTPException
    assert response["statusCode"] == 400
    assert body["error"] == "HTTP error occurred"
    assert body["details"] == "Test HTTP error"


@pytest.mark.skipif(True, reason="[TODO]")
@pytest.mark.exception
def test_token_utils_exception(token_utils_ng):

    # Anticipated messages
    ERROR_MESSAGE = "Get token failed"

    # Test the authenticate.
    response = token_utils_ng.get_token("AAA")
    # Obtain the contents of Body.
    print(response)

    # Assert Exception
    assert response["statusCode"] == 500
    assert ERROR_MESSAGE == body["error"]
