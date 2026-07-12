import os
import sys


def get_required_environment_variable(name: str) -> str:
    value = os.getenv(name)

    if not value:
        print(f"Error: required environment variable '{name}' is missing.")
        sys.exit(1)

    return value


def main() -> None:
    print(f"Raw APP_ENV value: {os.environ.get('APP_ENV')!r}")

    app_env = get_required_environment_variable("APP_ENV")
    demo_secret = get_required_environment_variable("DEMO_SECRET")

    print(f"Application environment: {app_env}")
    print("DEMO_SECRET is configured successfully.")

    # Never print the secret itself
    if demo_secret:
        print("The application can safely use the secret.")


if __name__ == "__main__":
    main()