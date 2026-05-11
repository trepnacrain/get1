import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 1
sampling_frequency = 100


if __name__ == "__main__":
    try:
        dac = pwm.PWM_DAC(12, 1000, 3.290, True)
        
        while True:
            try:
                dac.set_voltage((sg.get_sin_wave_amplitude(signal_frequency, 2)/2)*amplitude)
                time.sleep(1/sampling_frequency)

            except ValueError:
                print("Error")

    finally:
        dac.deinit()
