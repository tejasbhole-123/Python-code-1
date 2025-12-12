print("Hello, World!")
print("This is my second line!v4
print("This is my third linev5")
print("This is my forth line")
import requests
import json
import logging
from datetime import datetime

# ---------------------------------------
# Logging setup
# ---------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

# ---------------------------------------
# A simple utility function
# ---------------------------------------
def save_json(filename, data):
    """Save Python dict into a JSON file"""
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        logging.info(f"Data saved to {filename}")
    except Exception as e:
        logging.error(f"Unable to save file: {e}")

# ---------------------------------------
# A class with a method
# ---------------------------------------
class UserFetcher:
    """Fetch user data from JSONPlaceholder API"""

    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com/users"

    def get_users(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            logging.info("Fetched user list successfully")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            return []

# ---------------------------------------
# Main program logic
# ---------------------------------------
def main():
    logging.info("Program started")

    fetcher = UserFetcher()
    users = fetcher.get_users()

    # Save to JSON file
    save_json("users_output.json", users)

    # Show summary
    print(f"Fetched {len(users)} users at {datetime.now()}")

if __name__ == "__main__":
    main()
