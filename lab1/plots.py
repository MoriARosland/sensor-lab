import csv
import matplotlib.pyplot as plt
from raspi_import import raspi_import


def timeplot(filepath, channels=5):
    sample_period, data = raspi_import(filepath, channels)

    print(sample_period)
    print(data)

    return 0


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
