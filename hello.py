from datetime import datetime

import requests

def main() -> None:
    print("Hello from Python!")
    print("This program is running inside GitHub Actions")
    print(f"Current time: {datetime.now()}")

    response = requests.get(
        "https://api.github.com",
        timeout=10,
    )

    print(f"GitHub API status code: {response.status_code}")

    response.raise_for_status

    data = response.json()
    print(f"Current user API URL: {data['current_user_url']}")


if __name__ == "__main__":
    main()