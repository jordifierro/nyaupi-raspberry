import RPi.GPIO as GPIO
import time
import subprocess
import atexit
import os

def check():
    global door_process
    door_process = subprocess.Popen('python3 door.py', shell=True)
    while True:
        time.sleep(2)

def tear_down():
    global door_process
    door_process.kill()


if __name__ == '__main__':
    atexit.register(tear_down)
    check()
