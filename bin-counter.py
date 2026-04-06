import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]

for led in leds:
    GPIO.output(led, 0)

button_up = 9
GPIO.setup(button_up, GPIO.IN)
button_down = 10
GPIO.setup(button_down, GPIO.IN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GPIO.input(button_up):
        num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(button_down):
        num -= 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    GPIO.output(leds, dec2bin(num))