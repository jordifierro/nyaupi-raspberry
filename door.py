import RPi.GPIO as GPIO
import time
import os


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def watch():
    while True:
       if door_is_open():
           print('open')
       else:
           print('closed')
       time.sleep(2)

def door_is_open():
    return GPIO.input(8)

if __name__ == '__main__':
    setup()
    watch()
