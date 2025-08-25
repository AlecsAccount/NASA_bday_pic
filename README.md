NASA APOD Birthday Viewer
This Python script fetches and displays NASA’s Astronomy Picture of the Day (APOD) for a user’s birthday (or any date after June 16, 1995). It interacts with NASA’s public APOD API to retrieve the picture, title, explanation, and media link.
Features
•	Prompts the user for their birthday in YYYY-MM-DD format

•	Validates the date format and ensures it’s not earlier than June 16, 1995

•	Retrieves APOD data (image or video) from NASA’s API

•	Displays the title, date, explanation, and direct media link
Requirements
•	Python 3.7+

•	requests library
Install dependencies via:
pip install requests
Usage
1.	Clone or download this script.

2.	Open a terminal in the script’s directory.

3.	Run the script with:
python apod_birthday.py
4.	Enter your birthday (or any date from 1995-06-16 onwards) in the format:
YYYY-MM-DD
5.	The script will display the Astronomy Picture of the Day details for that date.

   
Example Output
Hello Human!
Go ahead and enter your birthday like this (YYYY-MM-DD): 2000-01-01

🌟 Astronomy Picture of the Day 🌟
Date: 2000-01-01
Title: A Starry Night in January
Explanation: [APOD explanation here...]
Media Type: image
Check the image out: https://apod.nasa.gov/apod/image/example.jpg
API Key
The script uses a demo NASA API key by default.
You can get your own API key from https://api.nasa.gov.
Limitations
•	Dates before June 16, 1995 are not supported (APOD started then).

•	Limited by NASA API rate limits (default key: 30 requests/hour).
Improvements in This Version
•	Removed duplicate API calls — the script now calls the API only once per valid date.

•	Removed redundant date checks — only one validation ensures the date is on/after June 16, 1995.

•	Consolidated duplicate output blocks into a single, clean section.

•	Simplified code flow for easier readability and maintenance.
License
This project is open-source. Feel free to modify and use it as needed.
