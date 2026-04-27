#import RPi.GPIO as GPIO
import pwm_dac as pwm
import signal_generator as sg 
import time

amplitude = 3.2
signal_freq = 10
sampling_freq = 1000

if __name__ == '__main__':
    try:
        dac = pwm.PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                dac.set_voltage((sg.get_sin_wave_amplitude(signal_freq, 2)/2)*amplitude)
                time.sleep(1/sampling_freq)
        
            except ValueError():
                print('Error')

    finally:
        dac.deinit()