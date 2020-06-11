import RPi.GPIO as GPIO
import time


def setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
  while True:
    if is_open():
       print("Door is open")
       time.sleep(2)
    if not is_open():
       print("Door is closed")
       time.sleep(2)

def is_open():
  return GPIO.input(8)

def destroy():
  pass

if __name__ == '__main__':
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    GPIO.cleanup()
    destroy()
