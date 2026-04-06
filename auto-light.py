import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.output)
f = 6
GPIO.setup(f, GPIO.input)
state = 0

while True:
    if GPIO.input(f):
        state = not state
        GPIO.output(led, state)

