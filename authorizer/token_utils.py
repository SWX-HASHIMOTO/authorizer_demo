from dotenv import load_dotenv
import json
import os
import logging
import http.client

if not os.getenv("AWS_LAMBDA_FUNCTION_NAME"):
    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    print(dotenv_path)
    load_dotenv(dotenv_path)

# Get value from environment variable
AUDIENCE = os.getenv("AUDIENCE")
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


class TokenUtils(object):
    """
    Class that issues Token for Auth0.
    """

    def __init__(self):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.audience = AUDIENCE
        self.auth0_domain = AUTH0_DOMAIN
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def get_token(self):
        """
        Function get token from Auth0.

        Returns:
            str: Token with Bearer (Bearer .*)

        Exception:
            Outputs an error if the acquisition of a token fails.
        """

        try:
            self.logger.info("Token is issued.")

            # Create payload
            payload_dic = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "audience": self.audience,
                "grant_type": "client_credentials",
            }

            self.logger.info(f"HTTPS Request:(POST) https://{self.auth0_domain}/oauth/token")
            # Obtain token by HTTP request to Auth0
            conn = http.client.HTTPSConnection(self.auth0_domain)
            payload = json.dumps(payload_dic)
            headers = {"content-type": "application/json"}
            conn.request("POST", "/oauth/token", payload, headers)
            res = conn.getresponse()
            data = res.read()
            return json.loads(data)

        except http.client.HTTPException as e:
            # Handle HTTP-related errors.
            self.logger.error(f"Error: HTTP error occurred {e}")

            return {
                "statusCode": 400,
                "body": json.dumps({"error": "HTTP error occurred", "details": str(e)}),
            }

        except Exception as e:
            # Other Error
            self.logger.error(f"Error: Get token failed {e}")

            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Get token failed", "details": str(e)}),
            }
