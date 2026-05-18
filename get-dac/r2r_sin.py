import RPi.GPIO as GPIO
import r2r_dac as r2r
import signal_generator as sg 
import time

amplitude = 3.2
signal_freq = 2
sampling_freq = 1000

if __name__ == '__main__':
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.1, True)

        while True:
            try:
                dac.set_voltage((sg.get_sin_wave_amplitude(signal_freq, 2)/2)*amplitude)
                sg.wait_for_sampling_period(sampling_freq)
                #time.sleep(sampling_freq)
            except ValueError:
                print('Error')

    finally:
        dac.deinit()
    

    

    
