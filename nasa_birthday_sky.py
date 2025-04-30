# This only works for dates >= June 16, 1995 

import requests
from datetime import datetime

# NASA APOD API URL and key
API_KEY = "" #Put your lovely API key here 
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
    # Get user's birthday
    birthday = input("\n  Hello Human! \n  Go aheand and enter your birthday like this (YYYY-MM-DD): ")
    
    # Validate date format
    try:
        datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        print("Cmon now that's not how I told you to enter it! Please use YYYY-MM-DD.")
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
