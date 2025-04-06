#!/bin/bash

cd ~/CortexShield/scripts

python run_all_processes.py

# Create a new tmux session named "AetherSafe" and start AetherMind in the same window
cd ~/CortexShield/scripts

python aethermind.py

tmux new-session -d -s AetherSafe "python ~/CortexShield/scripts/aethermind.py; bash"

# Send command to start SafeHarbor in the same window
cd ~/CortexShield/script

python SafeHarbor.py

tmux send-keys -t AetherSafe "python ~/CortexShield/scripts/safeharbor.py" C-m

# Send command to start main.py in the same window
cd ~/CortexShield/main.py

python main.py

tmux send-keys -t AetherSafe "python ~/CortexShield/scripts/main.py" C-m

# Send command to start Overwatch in the same window
cd ~/CortexShield/scripts

python Overwatch.py

tmux send-keys -t AetherSafe "python ~/CortexShield/scripts/Overwatch.py" C-m

# Send command to start Helm in the same window
cd ~/CortexShield/scripts

python Helm.py

tmux send-keys -t AetherSafe "python ~/CortexShield/scripts/Helm.py" C-m

# Send command to start TerminalMirrorSave in the same window
cd ~/CortexShield/modules

python terminalmirrorsave.py

tmux send-keys -t AetherSafe "python ~/CortexShield/modules/terminalmirrorsave.py" C-m

# Attach to the session so you can monitor all processes
tmux attach-session -t AetherSafe

