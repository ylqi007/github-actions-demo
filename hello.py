from datetime import datetime


def main() -> None:
    print("Hello from Python!")
    print("This program is running inside GitHub Actions")
    print(f"Current time: {datetime.now()}")


if __name__ == "__main__":
    main()