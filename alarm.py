import RPi.GPIO as GPIO
import time
import subprocess
import atexit
import os

from storage import status


door_process = None
buzzer_process = None
mail_process = None

def check():
    os.system('python3 storage.py')

    global door_process
    global buzzer_process
    door_process = subprocess.Popen('python3 door.py', shell=True)

    is_open_door = status()['door_open']
    is_alarm_active = status()['alarm_active']

    while True:

        is_now_alarm_active = status()['alarm_active']
        if not is_alarm_active and is_now_alarm_active:
            if buzzer_process is not None:
                buzzer_process.kill()
            buzzer_process = subprocess.Popen('python3 buzzer.py beep 2', shell=True)
        elif is_alarm_active and not is_now_alarm_active:
            if buzzer_process is not None:
                buzzer_process.kill()
            buzzer_process = subprocess.Popen('python3 buzzer.py beep 1', shell=True)

        is_now_open_door = status()['door_open']
        if not is_open_door and is_now_open_door and is_now_alarm_active:
            if buzzer_process is not None:
                buzzer_process.kill()
            ALARM_SOUND_SECONDS = int(os.environ['ALARM_SOUND_MINUTES']) * 60
            buzzer_process = subprocess.Popen('python3 buzzer.py alarm ' + str(ALARM_SOUND_SECONDS), shell=True)
            mail_process = subprocess.Popen('python3 mail.py', shell=True)

        is_alarm_active = is_now_alarm_active
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
