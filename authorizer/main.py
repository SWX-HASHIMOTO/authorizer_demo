import json
from libs.auth import authenticate

if __name__ == "__main__":

    try:
        print("START")
        data = authenticate(
            {
                "type": "TOKEN",
                "authorizationToken": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRkYVFKMzk1OHZZQkN5cVVJQVBIOSJ9.eyJpc3MiOiJodHRwczovL2Rldi1xeTVnaGJ6YTdrend4cHVjLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJEZEYxQXN2VU1uaUZXazB5czhoa1RMNzV3MUpUZUVCbkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9oY3lja3Ztd20yLmV4ZWN1dGUtYXBpLmFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20vIiwiaWF0IjoxNzM0OTUwOTQyLCJleHAiOjE3MzUwMzczNDIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6IkRkRjFBc3ZVTW5pRldrMHlzOGhrVEw3NXcxSlRlRUJuIn0.odt6CmPb7ewfxOxso9Dcl-rsddpk_XhvESHm7fbGiTu5xZIihfkDhnOmmlPXCUh4Ye1Id0KYSijb2PdruP7arQI0zu2EpNtYVQwIXjOVbLmMru1hizvnP2JUptz3hUZRzrAX_yyMtm6rTgbYzpNaAMPzcWBIHPodhtWupG3gIWxNQDeJQShCa8COMDZNa3Oeva-tlD7OWclEv6O7VPGzq66sOlPz5t4xaQJPhbrwlKj52YS5kX79wD2Uq_AavdRT2EObZQlHrqUtkcL-oJJ3nEU70QwyJBM9jioQhvOf1hVrQYN6o5xMqU5L4vQr133EQbbIH43tdWZpAJZONo8-Ug",
                "methodArn": "",
            }
        )

        print(json.dumps(data))

        print("END")

    except Exception as e:
        print(f"Unauthorized {str(e)}")
