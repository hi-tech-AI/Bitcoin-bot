import os

# Specify the path to the Chrome history file
history_file_path = 'C:/Users/Mishuka/AppData/Local/Google/Chrome/User Data/Default/History'

# Check if the history file exists
if os.path.exists(history_file_path):
    # Delete the history file
    os.remove(history_file_path)
    print("Chrome history deleted successfully.")
else:
    print("Chrome history file not found.")