import sys
import os
import psutil

def check_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

if __name__ == "__main__":
    process_name = "WebexHost.exe"  # Change the default process/program name here

    if len(sys.argv) >= 2:
        process_name = sys.argv[1]

    if check_process_running(process_name):
        print(f"The process '{process_name}' is still running.")
    else:
        print(f"The process '{process_name}' is not running.")
