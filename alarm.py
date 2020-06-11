import RPi.GPIO as GPIO
import time

import door
import buzzer

buzzing = False

def setup():
  door.setup()
  buzzer.setup()

def loop():
  global buzzing

  while True:

    if buzzing:
      buzzer.buzz()
    else:
      buzzer.silence()

    if door.is_open():
      buzzing = True
    if not door.is_open():
      buzzing = False 

def destroy():
  door.destroy()
  buzzer.destroy()

if __name__ == '__main__':
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()
