# codeecho.py
import datetime
import os

LOG_FILE = "codeecho_log.txt"

def log_command(command, response):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{timestamp}] COMMAND: {command}\nRESPONSE: {response}\n\n"
    with open(LOG_FILE, "a") as file:
        file.write(entry)

def clear_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

def read_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            return file.read()
    return "No logs found."
