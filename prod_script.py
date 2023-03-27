import time
import subprocess

while(True):
    subprocess.run(['python3', './eleccions_backend/eleccions_pipeline_backend.py'])
    print("Current time:", time.strftime("%H:%M:%S"))
    time.sleep(180)