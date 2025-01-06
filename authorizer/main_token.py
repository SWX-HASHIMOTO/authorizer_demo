import os
from dotenv import load_dotenv

from token_utils import TokenUtils

if __name__ == "__main__":

    try:
        print("START")
        token_utils = TokenUtils()

        token = token_utils.get_token()
        print(token)
        print("END")

    except Exception as e:
        print(f"Unauthorized {str(e)}")
