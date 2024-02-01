import csv
import matplotlib.pyplot as plt
import numpy as np
from raspi_import import raspi_import

voltage_ref = 3.3
bit_resolution = 2**12
adc_resolution = voltage_ref / bit_resolution

filepath_bin = "lab1/bin/sine.bin"


def timeplot_runner():
    timeplot(filepath_bin)


def timeplot(filepath, channels=5):
    sample_period, data = raspi_import(filepath, channels)

    data = data.transpose()  # convert to 5 x 31250 matrix

    time = np.arange(0, (len(data[0]) - 0.5) * sample_period, sample_period)

    # convert raw data to voltage
    voltage = data * adc_resolution
    time = time * 1e3  # scale time axis

    fig, axs = plt.subplots(channels, 1, figsize=(10, 8), sharex=True)

    colors = ['b', 'g', 'r', 'c', 'm']  # List of colors for each graph

    for i in range(channels):
        axs[i].plot(time, voltage[i], color=colors[i])  # Set color for each graph
        axs[i].set(xlim=(0, 10), ylim=(-0.01, 1.1), xlabel="Time [ms]", ylabel="Voltage [V]", title=f"ADC {i+1}")

    plt.tight_layout()
    plt.show()


def bodeplot(filepath):
    frequencies = []
    channel1_magnitude = []
    channel1_phase = []
    channel2_magnitude = []

    with open(filepath, mode='r') as file:
        csv_reader = csv.reader(file)

        next(csv_reader)  # skip first line in csv.

        for row in csv_reader:
            frequencies.append(float(row[0]))
            channel1_magnitude.append(float(row[1]))
            channel1_phase.append(float(row[2]))
            channel2_magnitude.append(float(row[3]))

    cutoff_frequency = 24

    plt.plot(frequencies, channel1_magnitude)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude [dB]")
    plt.title("Magnitude response")
    plt.axvline(x=cutoff_frequency, color='r', linestyle='--', label=f'Cutoff Frequency: ~{cutoff_frequency} Hz')
    plt.tight_layout()
    plt.xscale("log")
    plt.legend()

    plt.show()
