from authorizer.token_utils import TokenUtils


def generate_token():

    try:
        token_utils = TokenUtils()
        token = token_utils.get_token()
        return f"{token["token_type"]} {token["access_token"]}"

    except Exception as e:
        raise Exception


if __name__ == "__main__":

    try:
        token = generate_token()
        with open("./tests/token.txt", "w") as file:
            file.write(token)

    except Exception as e:
        print(f"Unauthorized {str(e)}")
