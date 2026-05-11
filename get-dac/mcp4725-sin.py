import mcp4725_driver as mcp
import signal_generator as sg
import time


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    try:
        dac = mcp.MCP4725(3.183, True)
        
        while True:
            try:
                dac.set_voltage((sg.get_sin_wave_amplitude(signal_frequency, 2)/2)*amplitude)
                time.sleep(1/sampling_frequency)

            except ValueError:
                print("Error")

    finally:
        mcp.deinit()

