import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend, butter, filtfilt
from scipy.fft import fftfreq, fftshift, fft

SAMPLING_RATE = 30  # Hz
NYQUIST = SAMPLING_RATE / 2

# Heart rate range: 30 - 150 BPM
CUTOFF_LOW = 0.5  # Hz
CUTOFF_HIGH = 2.5  # Hz


def calc_and_plot_fft(colorData):
    window = np.hanning(len(colorData))
    colorData = colorData * window

    colorData = detrend(colorData)

    f_low = CUTOFF_LOW / NYQUIST
    f_high = CUTOFF_HIGH / NYQUIST
    filter_order = 8

    b, a = butter(filter_order, [f_low, f_high], btype='band')
    filtered_colorData = filtfilt(b, a, colorData)

    NFFT = 2**20
    df = SAMPLING_RATE / NFFT

    X = np.fft.fft(filtered_colorData, NFFT)
    X = np.fft.fftshift(X)

    freqs = np.arange(-NYQUIST, NYQUIST, df)

    max_freq = freqs[np.argmax(np.abs(X))]
    print(f'max heartrate: {np.abs(max_freq * 60)} BPM')

    plt.figure()
    plt.plot(freqs, np.abs(X))
    plt.title('FFT')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.show()
