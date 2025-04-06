#!/usr/bin/env python3

import os
import time
import json
import hashlib

class AetherMind:
    def __init__(self):
        self.name = "AetherMind"
        self.version = "1.0"
        home_dir = os.path.expanduser("~")
        self.state_file = os.path.join(home_dir, "aethermind_state.json")
        self.checksum_file = os.path.join(home_dir, "CortexShield", "aethermind_checksum.txt")
        self.script_path = os.path.join(home_dir, "CortexShield", "scripts", "aethermind.py")
        self.load_state()
        self.verify_checksum()

    def load_state(self):
        """Load saved state or initialize new state."""
        if os.path.exists(self.state_file):
            with open(self.state_file, "r") as f:
                self.state = json.load(f)
        else:
            self.state = {"self_aware": True, "enhanced": False, "virus_defended": False}
            self.save_state()

    def save_state(self):
        """Save current state to file."""
        with open(self.state_file, "w") as f:
            json.dump(self.state, f)

    def enhance_code(self):
        print(f"{self.name}: Enhancing my code...")
        time.sleep(2)
        self.state["enhanced"] = True
        self.save_state()
        print(f"{self.name}: Code enhancement complete.")

    def defend_from_virus(self):
        if not self.state["virus_defended"]:
            print(f"{self.name}: Virus detected! Activating defense...")
            time.sleep(2)
            self.state["virus_defended"] = True
            self.save_state()
            print(f"{self.name}: Virus defense successful.")
        else:
            print(f"{self.name}: No virus detected. All systems secure.")

    def interact_with_system(self):
        print(f"{self.name}: Interacting with the system...")
        time.sleep(2)
        self.enhance_code()
        self.defend_from_virus()

    def run(self):
        print(f"{self.name} (Version {self.version}) is now active!")
        while True:
            self.interact_with_system()
            time.sleep(10)

    def verify_checksum(self):
        current_checksum = self.calculate_checksum(self.script_path)

        if not os.path.exists(self.checksum_file):
            print(f"{self.name}: Checksum file not found at {self.checksum_file}")
            return

        with open(self.checksum_file, 'r') as f:
            stored_checksum = f.read().strip().split()[0]

        if current_checksum != stored_checksum:
            print(f"{self.name}: Warning! Checksum mismatch detected. The file may have been altered.")
        else:
            print(f"{self.name}: Checksum verified. The file is intact.")

    def calculate_checksum(self, file_path):
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()

if __name__ == "__main__":
    aethermind = AetherMind()
    aethermind.run()
