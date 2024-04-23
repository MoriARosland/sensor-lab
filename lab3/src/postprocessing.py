import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend, butter, filtfilt
from scipy.signal.windows import hann

NFFT = 2**20

SAMPLING_FREQ = 40  # Hz
NYQUIST = SAMPLING_FREQ / 2

# Heart rate range: 65 - 90 BPM
CUTOFF_LOW = 1.08 / NYQUIST  # Hz normalized
CUTOFF_HIGH = 1.5 / NYQUIST  # Hz normalized


def calc_and_plot_fft(colorData, colorChannel):
    window = hann(len(colorData))
    colorData = colorData * window
    colorData = detrend(colorData)

    filter_order = 4
    b, a = butter(filter_order, Wn=[CUTOFF_LOW, CUTOFF_HIGH], btype='band')
    colorData = filtfilt(b, a, colorData)

    colorData_fft = np.fft.fft(colorData, NFFT)
    colorData_fft = np.fft.fftshift(colorData_fft)

    df = SAMPLING_FREQ / NFFT
    freqs = np.arange(-NYQUIST, NYQUIST, df)

    epsilon = 1e-10  # prevent division by zero

    # Use this for plotting
    spectrum = 20 * np.log10(abs(colorData_fft) /
                             (max(abs(colorData_fft)) + epsilon))
    # spectrum = abs(colorData_fft)  # Use this for SNR calculation

    middle = int(NFFT / 2)
    top = 5

    colorData_fft = colorData_fft[middle: int(middle + top / df)]
    spectrum = spectrum[middle: int(middle + top / df)]
    freqs = freqs[middle: int(middle + top / df)]

    heart_rate = freqs[np.argmax(spectrum)] * 60
    heart_rate = round(heart_rate * 100) / 100

    print(f'Heart rate: {heart_rate} BPM')

    calc_snr(spectrum, freqs, colorChannel)

    return heart_rate


def calc_snr(spectrumData, freqsX, colorChannel):
    # Reference: hr_reflektans/four.txt
    range_start = np.argmax(spectrumData) - 1000
    range_end = np.argmax(spectrumData) + 1000

    SNR = 2*np.mean(spectrumData[range_start:range_end]) / (
        np.mean(spectrumData[:range_start]) + np.mean(spectrumData[range_end:]))

    print(f'SNR: {SNR}')

    plt.figure(figsize=(12, 8))
    plt.plot(freqsX, spectrumData)
    plt.axvline(freqsX[range_start], linestyle='--', color='red', label=f'Range Start: {
                freqsX[range_start]:.2f} Hz ({freqsX[range_start]*60:.2f} BPM)')
    plt.axvline(freqsX[range_end], linestyle='--', color='green', label=f'Range End: {
                freqsX[range_end]:.2f} Hz ({freqsX[range_end]*60:.2f} BPM)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude (dB)')
    plt.title(f'FFT - Relative Effect Channel {colorChannel}')
    plt.legend()
    plt.show()


def colorData_timeplot(colorData, colorChannel):
    colorData = detrend(colorData)

    filter_order = 4
    b, a = butter(filter_order, [CUTOFF_LOW, CUTOFF_HIGH], btype='band')
    filtered_colorData = filtfilt(b, a, colorData)

    time = np.arange(0, len(colorData) / SAMPLING_FREQ, 1/SAMPLING_FREQ)

    plt.figure(figsize=(10, 6))
    plt.plot(time, colorData, alpha=0.5, label='Unfiltered Data')
    plt.plot(time, filtered_colorData, label='Filtered Data')
    plt.title(f'Time plot - Channel {colorChannel}')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
