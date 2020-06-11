import RPi.GPIO as GPIO
import time
import math

def setup():
  global p
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(7, GPIO.OUT)
  p = GPIO.PWM(7, 1)
  p.start(0);

def loop():
  while True:
    buzz()

def buzz():
  p.start(50)
  for x in range(0, 360):
    sinVal = math.sin(x * (math.pi / 180.0))
    toneVal = 2000 + sinVal * 500
    p.ChangeFrequency(toneVal)
    time.sleep(0.002)

def silence():
  p.ChangeFrequency(1)
  p.stop()

def destroy():
  GPIO.output(7, GPIO.LOW)

if __name__ == '__main__':
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()
    GPIO.cleanup()
