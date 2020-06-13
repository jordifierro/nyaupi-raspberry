import RPi.GPIO as GPIO
import time
import math
import atexit
import sys

PIN = 7

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.OUT)
    global p
    p = GPIO.PWM(PIN, 1)

def tear_down():
    global p
    p.ChangeFrequency(1)
    p.stop()
    GPIO.output(PIN, GPIO.LOW)

def beep(times):
    while (times > 0):
        global p
        p.start(50)
        p.ChangeFrequency(2000)
        time.sleep(0.1)
        p.ChangeFrequency(1)
        p.stop()
        times -= 1
        time.sleep(0.1)

def alarm(seconds):
    t_end = time.time() + seconds
    while time.time() < t_end:
        global p
        p.start(50)
        for x in range(0, 360):
            sinVal = math.sin(x * (math.pi / 180.0))
            toneVal = 2000 + sinVal * 500
            p.ChangeFrequency(toneVal)
            time.sleep(0.001)

if __name__ == '__main__':
    atexit.register(tear_down)
    setup()
    if (len(sys.argv) != 3):
        print("Use 'beep times' or 'alarm seconds'")
    elif (sys.argv[1] == "beep"):
        beep(int(sys.argv[2]))
    elif (sys.argv[1] == "alarm"):
        alarm(int(sys.argv[2]))
    else:
        print("Use 'beep times' or 'alarm seconds'")
