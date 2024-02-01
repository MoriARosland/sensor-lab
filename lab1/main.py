import csv
import matplotlib.pyplot as plt
from raspi_import import raspi_import
from fft import calc_fft_windowed, calc_normalized_power_spectrum, generate_freq_array

frequencies = []
channel1_magnitude = []
channel1_phase = []
channel2_magnitude = []


with open('lab1/data/filtermaling2.csv', mode='r') as file:
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
