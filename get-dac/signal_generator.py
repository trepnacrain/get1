import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    amp = np.sin(2*np.pi*freq*time)
    return (amp + 1) / 2

def wait_for_sampling_period(sampling_freq):
    time.sleep(1/sampling_freq)

