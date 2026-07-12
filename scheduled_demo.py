import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def main() -> None:
    event_name = os.getenv("GITHUB_EVENT_NAME", "local")

    utc_now = datetime.now(timezone.utc)
    seattle_now = utc_now.astimezone(ZoneInfo("America/Los_Angeles"))

    print("Scheduled workflow demo")
    print(f"Trigger event: {event_name}")
    print(f"Current UTC time: {utc_now.isoformat()}")
    print(f"Current Seattle time: {seattle_now.isoformat()}")
    print("The scheduled task ran successfully.")


if __name__ == "__main__":
    main()