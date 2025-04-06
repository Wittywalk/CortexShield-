#!/usr/bin/env python3
import os
import time
import shutil
import hashlib
from datetime import datetime

class Overwatch:
    def __init__(self):
        self.name = "Overwatch"
        self.version = "1.0"

        home_dir = os.getenv("HOME")
        self.file_path = os.path.join(home_dir, "CortexShield/scripts/AetherMind.py")
        self.checksum_file = os.path.join(home_dir, "CortexShield/scripts/aethermind_checksum.txt")
        self.backup_dir = os.path.join(home_dir, "CortexShield/backups")

    def check_file_integrity(self):
        try:
            with open(self.file_path, 'rb') as file:
                file_data = file.read()
                file_hash = hashlib.sha256(file_data).hexdigest()

            with open(self.checksum_file, 'r') as f:
                saved_hash = f.read().strip()

            return file_hash == saved_hash
        except Exception as e:
            print(f"Error checking integrity: {e}")
            return False

    def perform_backup(self):
        try:
            if not os.path.exists(self.backup_dir):
                os.makedirs(self.backup_dir)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"AetherMind_backup_{timestamp}.py"
            backup_path = os.path.join(self.backup_dir, backup_name)

            shutil.copy2(self.file_path, backup_path)
            print(f"Backup created at: {backup_path}")
        except Exception as e:
            print(f"Error creating backup: {e}")

    def monitor_system(self):
        while True:
            if not self.check_file_integrity():
                print("Integrity check failed! Backing up modified file...")
                self.perform_backup()
            time.sleep(60)

    def run(self):
        print(f"{self.name} (Version {self.version}) is now active!")
        self.monitor_system()

if __name__ == "__main__":
    overwatch = Overwatch()
    overwatch.run()
