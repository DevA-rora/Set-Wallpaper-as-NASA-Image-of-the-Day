# Import os to use applescript:
import os

path = input("Path to the images: ")
command = f""" osascript -e '

tell application "Finder" to set desktop picture to POSIX file "{path}"

' """

os.system(command)
