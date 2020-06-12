import RPi.GPIO as GPIO
import time
import math

class Buzzer:

    PIN = 7

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PIN, GPIO.OUT)
        self.p = GPIO.PWM(self.PIN, 1)
        self.p.start(0);

    def tear_down(self):
        self.p.ChangeFrequency(1)
        self.p.stop()
        GPIO.output(self.PIN, GPIO.LOW)
        GPIO.cleanup()

    def run(self, func, *args, **kwargs):
        self.setup()
        func(*args, **kwargs)
        self.tear_down()

    def beep(self, times):
        self.run(self._beep, times)

    def alarm(self, seconds):
        self.run(self._alarm, seconds)

    def _beep(self, times):
        while (times > 0):
            self.p.start(50)
            self.p.ChangeFrequency(2000)
            time.sleep(0.1)
            self.p.ChangeFrequency(1)
            self.p.stop()
            times -= 1
            time.sleep(0.1)

    def _alarm(self, seconds):
        t_end = time.time() + seconds
        while time.time() < t_end:
            self.p.start(50)
            for x in range(0, 360):
                sinVal = math.sin(x * (math.pi / 180.0))
                toneVal = 2000 + sinVal * 500
                self.p.ChangeFrequency(toneVal)
                time.sleep(0.001)

if __name__ == '__main__':
    buzzer = Buzzer()
    try:
        buzzer.beep(1)
    except KeyboardInterrupt:
        buzzer.tear_down()
