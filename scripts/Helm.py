import subprocess
import time
import os

# Get the full path to the script directory
SCRIPT_DIR = os.path.expanduser("~/CortexShield/scripts")

# Function to start AetherMind and SafeHarbor processes
def start_processes():
    try:
        print("Starting AetherMind...")
        subprocess.Popen(["python3", os.path.join(SCRIPT_DIR, "AetherMind.py")])

        print("Starting SafeHarbor...")
        subprocess.Popen(["python3", os.path.join(SCRIPT_DIR, "SafeHarbor.py")])
    except Exception as e:
        print(f"Error starting processes: {e}")

# Function to stop AetherMind and SafeHarbor processes
def stop_processes():
    try:
        print("Stopping AetherMind...")
        subprocess.run(["pkill", "-f", "AetherMind.py"])

        print("Stopping SafeHarbor...")
        subprocess.run(["pkill", "-f", "SafeHarbor.py"])
    except Exception as e:
        print(f"Error stopping processes: {e}")

# Function to perform a strategic action
def perform_action(action):
    if action == "start":
        start_processes()
    elif action == "stop":
        stop_processes()
    elif action == "status":
        print("Checking system status...")
        subprocess.run(["ps", "aux"])  # You can customize this
    else:
        print("Invalid action!")

# Main entry point
if __name__ == "__main__":
    print("Helm is now running and awaiting your commands...")

    while True:
        action = input("Enter an action (start/stop/status): ").strip().lower()
        perform_action(action)
        time.sleep(1)
