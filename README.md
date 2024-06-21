# NASA APOD Wallpaper Setter
This project contains a Python script and Apple Shortcuts that will change your wallpaper to NASA'S Astrology Picture of the Day (APOD)

## Requirements

- Python 3.8 or higher
- Requests
- Python-Dotenv
  - *Optional, but it's a good idea to use it to store your API key*
- DateTime
- See `requirements.txt` for the exact versions

## Installation
### IOS Shortcut:


### MacOS Python Script

It is preferable to create a venv environment to install your packages independently from the rest of your local machine. 

learn how to create .venv here: [venv — Creation of virtual environments — Python 3.12.4 documentation](https://docs.python.org/3/library/venv.html)

1. Clone the repository:
    ```sh
    git clone https://github.com/DevA-rora/Set-Wallpaper-as-NASA-Image-of-the-Day.git
    cd Set-Wallpaper-as-NASA-Image-of-the-Day.git
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your NASA API key:
    ```sh
    API_KEY=your_nasa_api_key
    ```

## Usage

Run the script to download the APOD image for the current date and set it as the desktop wallpaper:

```sh
python main.py
```
