from datetime import date
import requests
import shutil
import os
from dotenv import find_dotenv, load_dotenv

# Load .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")
BASE_URL = 'https://api.nasa.gov/planetary/apod'

today = date.today()
print(f"Today's date {today}")

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
        apod_data = response.json()
        image_url = apod_data['hdurl'] if hd and 'hdurl' in apod_data else apod_data['url']
        
        # Download the image
        image_response = requests.get(image_url, stream=True)
        if image_response.status_code == 200:
            with open('apod_image.jpg', 'wb') as f:
                image_response.raw.decode_content = True
                shutil.copyfileobj(image_response.raw, f)
            
            return apod_data, 'apod_image.jpg'
        else:
            return apod_data, None
    else:
        response.raise_for_status()

if __name__ == '__main__':
    # Example usage
    try:
        apod_data, image_filename = get_apod(date='2023-06-20', hd=True)
        if image_filename:
            print(f"Title: {apod_data['title']}")
            print(f"Date: {apod_data['date']}")
            print(f"Explanation: {apod_data['explanation']}")
            print(f"HD Image URL: {apod_data['hdurl']}")
            print(f"Regular Image URL: {apod_data['url']}")
            print(f"Downloaded Image: {image_filename}")
        else:
            print(f"Title: {apod_data['title']}")
            print(f"Date: {apod_data['date']}")
            print(f"Explanation: {apod_data['explanation']}")
            print(f"Regular Image URL: {apod_data['url']}")
            print("Failed to download HD image.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")