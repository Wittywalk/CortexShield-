# terminal_mirror_save.py
import subprocess
import datetime

MIRROR_LOG = "terminal_mirror_output.txt"

def run_and_mirror(command):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        result = f"[{timestamp}] $ {command}\n{output}\n"
    except subprocess.CalledProcessError as e:
        result = f"[{timestamp}] $ {command}\nERROR: {e.output}\n"

    with open(MIRROR_LOG, "a") as f:
        f.write(result)

    return result

def clear_mirror_log():
    with open(MIRROR_LOG, "w") as f:
        f.write("")

def read_mirror_log():
    with open(MIRROR_LOG, "r") as f:
        return f.read()
