import subprocess
import time
import os
from SafeHarbor import SafeHarbor
    
    def main()

        firewall = SafeHarbor()
        firewall.run()

    if __name__ == "__main__":
        main()
# Importing AetherMind class
from AetherMind import AetherMind
import time

def run_all_processes():
    # Initialize AetherMind
    aethermind = AetherMind()

    # Start AetherMind's main functionality
    aethermind.run()

if __name__ == "__main__":
    run_all_processes()

class CortexShieldApp:
    def __init__(self):
        # Define the scripts and their paths
        self.scripts = {
            'AetherMind': '~/CortexShield/scripts/aethermind.py',
            'SafeHarbor': '~/CortexShield/scripts/safeharbor.py',
            'Main': '~/CortexShield/main.py',
            'Overwatch': '~/CortexShield/scripts/Overwatch.py',
            'Helm': '~/CortexShield/scripts/helm.py',
            'TerminalMirrorSave': '~/CortexShield/modules/terminal_mirror_save.py',  # Corrected script name
        }

        # Backup directory
        self.backup_directory = os.path.expanduser("~/CortexShield/backups")
        os.makedirs(self.backup_directory, exist_ok=True)

    def run_process(self, script_name):
        """Run a script process."""
        print(f"Starting process: {script_name}...")
        script_path = self.scripts.get(script_name)
        if script_path:
            subprocess.Popen(["python3", os.path.expanduser(script_path)])
        else:
            print(f"Script {script_name} not found.")

    def start_cortexshield(self):
        """Start all CortexShield scripts."""
        print("Starting CortexShield...")
        for script_name in self.scripts:
            self.run_process(script_name)
        self.log_event("CortexShield app processes started.")

    def log_event(self, message):
        """Log event to console."""
        timestamp = time.strftime("%Y-%m-%d
