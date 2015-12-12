import RPi.GPIO as GPIO
import time
from urllib.request import urlopen
import sys

sensor = 4


GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
    time.sleep(0.001)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        if new_state== "HIGH":
                        localtime=time.asctime(time.localtime(time.time()))
                        print ("intrusion detected at local time",localtime)
                        urlopen("https://docs.google.com/forms/d/1OvMU9v4GYL6BMX_9V2JxwwiXgupvT2pR-HueGl-j2ZU/formResponse?ifq&entry.1963731240=yes&submit=Submit")

