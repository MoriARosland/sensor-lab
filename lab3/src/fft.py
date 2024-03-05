import numpy as np
import matplotlib.pyplot as plt


def plot_spectrum(data, N_FFT, Fs):
    fft_result = np.fft.fft(data, N_FFT)
    freq = np.fft.fftfreq(N_FFT, 1 / Fs)

    print(f'Max frequency at: {freq[np.argmax(np.abs(fft_result))]} Hz')
    print(f'Heart rate: {freq[np.argmax(np.abs(fft_result))]*60} BPM')

    plt.plot(freq, np.abs(fft_result))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('FFT of Sine Wave')
    plt.show()
