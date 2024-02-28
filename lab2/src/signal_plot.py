import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend

from raspi_import import raspi_import

voltage_ref = 3.3
bit_resolution = 2**12
adc_resolution = voltage_ref / bit_resolution

filepath_bin = "/Users/rosland/development/sensor-lab/lab2/data/corrData/0deg.bin"


def timeplot(filepath, channels=5):
    sample_period, data = raspi_import(filepath, channels)

    for i in range(2, 5):
        data[:, i] = detrend(data[:, i])

    data = data.transpose()  # convert to 5 x 31250 matrix

    time = np.arange(0, (len(data[0]) - 0.5) * sample_period, sample_period)

    # convert raw data to voltage
    voltage = data * adc_resolution
    time = time * 1e3  # scale time axis

    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    colors = ['b', 'g', 'r', 'c', 'm']  # List of colors for each graph

    for i in range(2, 5):
        axs[i-2].plot(time, voltage[i], color=colors[i])  # Set color for each graph
        axs[i-2].set(xlim=(890, 960), xlabel="Time [ms]", ylabel="Voltage [V]", title=f"ADC {i+1}")
    plt.tight_layout()
    plt.show()


timeplot(filepath_bin)
