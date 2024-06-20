import requests
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Your NASA API key
API_KEY = os.getenv("API_KEY")

# Base URL for the APOD API
BASE_URL = 'https://api.nasa.gov/planetary/apod'

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

if __name__ == '__main__':
    # Example usage
    try:
        apod_data = get_apod(date='2023-06-20')
        print(f"Title: {apod_data['title']}")
        print(f"Date: {apod_data['date']}")
        print(f"Explanation: {apod_data['explanation']}")
        print(f"URL: {apod_data['url']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
