import RPi.GPIO as GPIO
import time
import os

from storage import set_door_open


PIN = int(os.environ['DOOR_SENSOR_PIN'])

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def watch():
    while True:
       if door_is_open():
           set_door_open(True)
       else:
           set_door_open(False)
       time.sleep(1)

def door_is_open():
    return GPIO.input(PIN)

if __name__ == '__main__':
    setup()
    watch()
