import RPi.GPIO as GPIO
import time

def strobe(pin1,pin2):
        GPIO.output(pin1,GPIO.HIGH)
        time.sleep(.05)
        GPIO.output(pin1,GPIO.LOW)
        time.sleep(.05)
        GPIO.output(pin2,GPIO.HIGH)
        time.sleep(.05)
        GPIO.output(pin2,GPIO.LOW)
        time.sleep(.05)
        return

GPIO.setmode(GPIO.BCM)

# example run
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

for i in range(0,50):
        strobe(17,18)

GPIO.cleanup()
