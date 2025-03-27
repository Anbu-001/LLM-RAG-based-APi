import os
import psutil
import subprocess

def open_calculator():
    """Opens the calculator application"""
    os.system("calc")

def get_cpu_usage():
    """Returns the current CPU usage percentage"""
    return psutil.cpu_percent(interval=1)

def open_chrome():
    """Opens Google Chrome"""
    os.system("start chrome")

def run_shell_command(command):
    """Executes a shell command"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
