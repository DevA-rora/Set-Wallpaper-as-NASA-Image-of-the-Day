import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
print(dotenv_path)

# Load the entries as environment variables:
load_dotenv(dotenv_path)

print()

API_KEY = os.getenv("API_KEY")
print(API_KEY)