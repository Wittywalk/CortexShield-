from codeecho import CodeEcho
from terminal_mirror_save import TerminalMirrorSave
import time
import subprocess

# Android permission handling (only runs on Android)
try:
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.INTERNET,
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE
    ])
except ImportError:
    print("Running outside of Android environment. Skipping permission request.")

# Initialize logging tools
codeecho = CodeEcho("aethermind_log.log")
terminal_mirror = TerminalMirrorSave("terminal_output.log")

# Log key startup events
codeecho.run_echo("AetherMind has started.")
time.sleep(1)
codeecho.run_echo("SafeHarbor has been activated.")
time.sleep(1)

# Capture and mirror terminal output
terminal_mirror.capture_terminal_output()

# Simulate some tasks and log them
for i in range(5):
    terminal_mirror.save_output(f"Running process {i + 1}...")
    time.sleep(2)
    codeecho.run_echo(f"Process {i + 1} completed.")

# Start other monitoring scripts
overwatch_process = subprocess.Popen(["python3", "Overwatch.py"])
helm_process = subprocess.Popen(["python3", "Helm.py"])

# Optionally wait for these to complete
overwatch_process.wait()
helm_process.wait()
