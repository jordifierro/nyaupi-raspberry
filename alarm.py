import RPi.GPIO as GPIO
import time
import subprocess
import atexit
import os

from status import status

door_process = None
buzzer_process = None

def check():
    global door_process
    global buzzer_process
    door_process = subprocess.Popen('python3 door.py', shell=True)
    is_open_door = status()['door_open']
    while True:
        is_now_open_door = status()['door_open']
        is_now_alarm_active = status()['alarm_active']
        if not is_open_door and is_now_open_door and is_now_alarm_active:
            if buzzer_process is not None:
                buzzer_process.kill()
            buzzer_process = subprocess.Popen('python3 buzzer.py alarm 5', shell=True)

        is_open_door = is_now_open_door

        time.sleep(0.5)

def tear_down():
    global door_process
    if door_process is not None:
        door_process.kill()
    global buzzer_process
    if buzzer_process is not None:
        buzzer_process.kill()


if __name__ == '__main__':
    atexit.register(tear_down)
    check()
