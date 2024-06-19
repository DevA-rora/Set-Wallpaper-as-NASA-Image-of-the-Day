# Goal: find the daily nasa photo and set it as the wallpaper for the macbook:

# Import os to use applescript, a language from apple that can interact with native system components:
import os

path = "/Users/devarora/Documents/Wallpapers/minimal-background.jpeg"
command = f""" osascript -e '

tell application "Finder" to set desktop picture to POSIX file "{path}"

' """

os.system(command)