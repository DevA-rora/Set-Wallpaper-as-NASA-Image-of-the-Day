# Import os to use applescript:
import os
import requests
from dotenv import load_dotenv, find_dotenv

# Load API key from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


# Your NASA API key
API_KEY = os.getenv("API_KEY")
# Base URL for the APOD API
BASE_URL = 'https://api.nasa.gov/planetary/apod'

# NASA Apod API function:
def get_apod(date=None, hd=False, concept_tags=False, count=None, start_date=None, end_date=None, thumbs=False):
    params = {
        'api_key': API_KEY,
        'hd': hd,
        'concept_tags': concept_tags,
        'thumbs': thumbs
    }
    
    if date:
        params['date'] = date
    if count:
        params['count'] = count
    if start_date:
        params['start_date'] = start_date
    if end_date:
        params['end_date'] = end_date

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return response.raise_for_status()


# Ask the user for the path where they would like to save their images:
user_path = input("Enter the path where you would like to save your NASA images: ")

# Create the the .txt file for the path to the images so that the user doesn't need to specify it again.

# Check if the path.txt file already exists:
if os.path.exists("path.txt") is True:
    pass
else:
    with open("path.txt", "w") as file:
        file.write(user_path)

# Applescript code (the stuff that changes the desktop wallpaper)
path = input("Path to the desired image: ")
command = f""" osascript -e '

tell application "Finder" to set desktop picture to POSIX file "{path}"

' """

os.system(command)
