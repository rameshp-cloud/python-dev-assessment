import requests


def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(
                f"Error: API request failed "
                f"with status code {response.status_code}."
            )
            return None

        users = response.json()

        if not isinstance(users, list):
            print("Error: Unexpected data format received from the API.")
            return None

        for user in users[:num_users]:
            try:
                print("Name:", user["name"])
                print("Email:", user["email"])
                print("City:", user["address"]["city"])
                print()
            except (KeyError, TypeError):
                print("Error: Unexpected data format received from the API.")
                return None

        return None

    except requests.exceptions.RequestException as error:
        print(f"Error: Could not connect to the API: {error}")
        return None


fetch_and_display_users(3)
