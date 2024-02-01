import numpy as np


def calc_normalized_power_spectrum(data, N_fft):

    X_f = np.fft.fft(data, N_fft)
    X_f = np.fft.fftshift(X_f)

    S_x = 20*np.log10(abs(X_f))  # Power in decibel
    S_x_normalized = S_x - np.max(S_x)

    return S_x_normalized


def calc_fft_windowed(data, N_fft):
    data_windowed = data * np.hanning(len(data))

    if len(data) < N_fft:
        data_padded = np.pad(data, (0, N_fft - len(data)), 'constant')
        data_padded_window = np.pad(data_windowed, (0, N_fft - len(data_windowed)), 'constant')
    else:
        data_padded = data
        data_padded_window = data_windowed

    data_windowed_fft = np.fft.fft(data_windowed, N_fft)

    return data_windowed_fft
