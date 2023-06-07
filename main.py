import subprocess

def get_monitors():
    lis = []
    monitors = subprocess.check_output("xrandr | grep ' connected ' | awk '{ print$1 }' ", shell=True).decode()
    lis = monitors.split() 
    print(lis)


get_monitors()
