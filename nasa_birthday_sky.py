import requests
from datetime import datetime

# NASA APOD API URL and key
API_KEY = "YOUR API KEY"
API_URL = "https://api.nasa.gov/planetary/apod"

def get_apod(date: str):
    """Fetch APOD data for a specific date."""
    params = {
        "api_key": API_KEY,
        "date": date
    }
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from NASA API.")
        print("Status Code:", response.status_code)
        print("Message:", response.json().get("error", {}).get("message", "Unknown error"))
        return None

def main():
    # Loop until valid date is entered
    while True:
        birthday = input("\n  Hello Human! \n  Go ahead and enter your birthday like this (YYYY-MM-DD): ")
        
        # Validate date format
        try:
            birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            print("Cmon now that's not how I told you to enter it! Please use YYYY-MM-DD.")
            continue  # Ask again

        # Check if date is before June 16, 1995
        earliest_date = datetime(1995, 6, 16)
        if birthday_date < earliest_date:
            print("Sorry, not to be mean but your birthday is older than when NASA began the photo of the day idea 😅")
            print("Try a date on or after 1995-06-16. Maybe choose a special day you remember fondly!")
            continue  # Ask again

        # Valid date
        break

    # Fetch and display APOD data
    data = get_apod(birthday)

    if data:
        print("\n🌟 Astronomy Picture of the Day 🌟")
        print("Date:\n", data.get("date"))
        print("Title:\n", data.get("title"))
        print("Explanation:\n", data.get("explanation"))
        print("Media Type:\n", data.get("media_type"))
        if data.get("media_type") == "image":
            print("Check the image out:", data.get("hdurl") or data.get("url"))
        else:
            print("Video URL:", data.get("url"))

    # Check if date is before June 16, 1995 - NASA didn't do photo of the day before then 
    earliest_date = datetime(1995, 6, 16)
    if birthday_date < earliest_date:
        print("Sorry, not to be mean but your birthday is older than when NASA began the photo of the day idea 😅")
        print("Try a date on or after 1995-06-16. Maybe choose a special day you remember fondly!")
        return

    data = get_apod(birthday)

    if data:
        print("\n🌟 Astronomy Picture of the Day 🌟")
        print("Date:", data.get("date"))
        print("Title:", data.get("title"))
        print("Explanation:", data.get("explanation"))
        print("Media Type:", data.get("media_type"))
        if data.get("media_type") == "image":
            print("Check the image out:", data.get("hdurl") or data.get("url"))
        else:
            print("Video URL:", data.get("url"))

if __name__ == "__main__":
    main()

