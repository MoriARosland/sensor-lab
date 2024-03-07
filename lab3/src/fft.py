import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend, butter, filtfilt
from scipy.signal.windows import hann

NFFT = 2**20

SAMPLING_FREQ = 40  # Hz
NYQUIST = SAMPLING_FREQ / 2

# Heart rate range: 30 - 120 BPM
CUTOFF_LOW = 0.5 / NYQUIST  # Hz normalized
CUTOFF_HIGH = 3 / NYQUIST  # Hz normalized


def calc_and_plot_fft(colorData):
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

    spectrum = spectrum = 20 * np.log10(abs(colorData_fft) / max(abs(colorData_fft)))

    middle = int(NFFT / 2)
    top = 5

    colorData_fft = colorData_fft[middle: int(middle + top / df)]
    spectrum = spectrum[middle: int(middle + top / df)]
    freqs = freqs[middle: int(middle + top / df)]

    pulse = freqs[np.argmax(spectrum)] * 60
    pulse = round(pulse * 100) / 100
    print(f'Pulse: {pulse} BPM')

    # plt.figure()
    # plt.plot(freqs, spectrum)
    # plt.title('Color Data FFT')
    # plt.xlabel('Frequency (Hz)')
    # plt.ylabel('Amplitude (dB)')
    # plt.show()

    return pulse


def calc_snr(spectrumData, freqsX):
    range_start = np.argmax(spectrumData) - 5000
    range_end = np.argmax(spectrumData) + 5000

    SNR = np.sum(spectrumData[range_start:range_end]) / (
        np.sum(spectrumData[:range_start]) + np.sum(spectrumData[range_end:])
    )

    print(f'SNR: {SNR}')

    plt.figure()
    plt.plot(freqsX, spectrumData)
    plt.axvline(freqsX[range_start])
    plt.axvline(freqsX[range_end])
    plt.show()


def colorData_timeplot(colorData):
    colorData = detrend(colorData)

    filter_order = 4
    b, a = butter(filter_order, [CUTOFF_LOW, CUTOFF_HIGH], btype='band')
    filtered_colorData = filtfilt(b, a, colorData)

    time = np.arange(0, len(colorData) / SAMPLING_FREQ, 1/SAMPLING_FREQ)

    plt.figure()
    plt.plot(time, colorData)
    plt.plot(time, filtered_colorData)
    plt.title('Time plot')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()
