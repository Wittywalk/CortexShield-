# terminal_mirror_save.py
import subprocess
import time

class TerminalMirrorSave:
    def __init__(self, log_file):
        self.log_file = log_file

    def save_output(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as log:
            log.write(f"[{timestamp}] {message}\n")
            print(f"Mirrored: {message}")

    def capture_terminal_output(self):
        # Example: Capture terminal commands and outputs using subprocess
        process = subprocess.Popen(['echo', 'Terminal session started...'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Write stdout and stderr to the log
        self.save_output(stdout.decode('utf-8'))
        if stderr:
            self.save_output(stderr.decode('utf-8'))
