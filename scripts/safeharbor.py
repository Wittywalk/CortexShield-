import os
import time
import subprocess
import threading

class SafeHarbor:
    def __init__(self):
        print("SafeHarbor (Version 1.0) is now active!")

    def check_for_intrusions(self):
        try:
            # Check running processes
            print("\nSafeHarbor: Checking for unusual processes...")
            process = subprocess.Popen(["ps"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            if error:
                print(f"SafeHarbor Error (ps): {error.decode('utf-8')}")
                return

            processes = output.decode("utf-8").splitlines()
            suspicious_processes = [proc for proc in processes if "python" in proc]

            if suspicious_processes:
                print("Suspicious processes found:")
                for proc in suspicious_processes:
                    print(f"  > {proc}")
            else:
                print("No suspicious processes found.")

            # Check for open network connections using netstat if lsof isn't available
            print("SafeHarbor: Checking for network connections...")
            try:
                process = subprocess.Popen(["lsof", "-i"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except FileNotFoundError:
                process = subprocess.Popen(["netstat", "-an"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            output, error = process.communicate()

            if error:
                print(f"SafeHarbor Error (network): {error.decode('utf-8')}")
                return

            connections = output.decode("utf-8").splitlines()
            if connections:
                print("Open network connections:")
                for conn in connections:
                    print(f"  > {conn}")
            else:
                print("No open network connections found.")

        except Exception as e:
            print(f"SafeHarbor General Error: {e}")

    def run(self):
        while True:
            self.check_for_intrusions()
            time.sleep(10)  # Check every 10 seconds

def start_safeharbor_in_thread():
    firewall = SafeHarbor()
    thread = threading.Thread(target=firewall.run)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    start_safeharbor_in_thread()
    # Keep the main thread alive
    while True:
        time.sleep(1)
