import numpy as np
import time
import math 

start = float(time.time())

def get_sin_wave_amplitude(freq, time):
    #sin_val = math.sin(2*math.pi*freq*(float(time.time())-start)) +1
    amp = np.sin(2*np.pi*freq*time)
    return (amp + 1) / 2
    #return sin_val

def wait_for_sampling_period(sampling_freq):
    time.sleep(1/sampling_freq)

