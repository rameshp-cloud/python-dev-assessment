import requests


def fetch_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("Error: API request failed.")
            return

        users = response.json()

        for user in users[:num_users]:
            try:
                print("Name:", user["name"])
                print("Email:", user["email"])
                print("City:", user["address"]["city"])
                print()

            except (KeyError, TypeError):
                print("Error: Unexpected data format received from the API.")

    except requests.exceptions.RequestException:
        print("Error: Could not connect to the API.")


fetch_users(3)