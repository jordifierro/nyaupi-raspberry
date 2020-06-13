import RPi.GPIO as GPIO
import time
import os

from status import set_door_open


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def watch():
    while True:
       if door_is_open():
           set_door_open(True)
       else:
           set_door_open(False)
       time.sleep(1)

def door_is_open():
    return GPIO.input(8)

if __name__ == '__main__':
    setup()
    watch()
