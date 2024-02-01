import plots as plt
import fft
import numpy as np
from raspi_import import raspi_import

filepath_bin = "lab1/bin/sine.bin"
filepath_data = "lab1/data/filtermaling2.csv"

N_fft = 4096 * 2

sample_period, data = raspi_import(filepath_bin)
data = data.transpose()


plt.bodeplot(filepath_data)
plt.timeplot_runner()

S_x = fft.calc_normalized_power_spectrum(data[0], N_fft)
plt.spectrum_plot(S_x, sample_period, "Power Spectrum")

X_f = fft.calc_spectrum(data[0], N_fft)
X_f_hanning = X_f * np.hanning(N_fft)

plt.spectrum_plot(X_f_hanning, sample_period, "Spectrum with Hanning Window")
