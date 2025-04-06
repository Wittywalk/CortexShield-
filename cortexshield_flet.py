import flet as ft
import subprocess
import time
from terminal_mirror_save import TerminalMirrorSave
from codeecho import CodeEcho
import threading

# Initialize necessary classes
codeecho = CodeEcho("aethermind_log.log")
terminal_mirror = TerminalMirrorSave("terminal_output.log")

def main(page: ft.Page):
    page.title = "CortexShield"
    page.add(ft.Text("Welcome to CortexShield"))

    output_area = ft.Column()

    page.add(output_area)

    # Function to run processes in the background and update UI
    def run_processes():
        # Example: Run some echo function
        codeecho.run_echo("AetherMind has started.")
        # You can replace this with the actual terminal commands you want to run
        subprocess.run(["echo", "Running background task"], stdout=subprocess.PIPE)

        # Once a process is done, you can update the UI
        terminal_mirror.save_to_log("Process finished.")  # Example log save

        # Update output on UI
        output_area.controls.append(ft.Text("Background task completed."))
        page.update()  # This will trigger the UI update

    # Start the process in the background using threading
    threading.Thread(target=run_processes, daemon=True).start()

# Start Flet app
ft.app(target=main)
