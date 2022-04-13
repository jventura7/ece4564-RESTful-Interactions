#ECE 4564

# figure out how to get a canvas token

# figure out PWN stuff on RPi GPIO pins
    # on/off
    # color - red/green/blue/magenta/cyan/yellow/white
    # brightness

# get flask services set up
import requests as requests
#10.0.0.101/24

ip_addr = "10.0.0.101"
port = "24"
r = requests.get("http://" + ip_addr + ":" + port + "/LED?status=on&color=red&intensity=50")