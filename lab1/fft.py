import numpy as np


def calc_normalized_power_spectrum(data, N_fft):

    X_f = np.fft.fft(data, N_fft)

    S_x = 20*np.log10(abs(X_f))  # Power in decibel
    S_x_normalized = S_x - np.max(S_x)
    S_x_normalized_shifted = np.fft.fftshift(S_x_normalized)

    return S_x_normalized_shifted


def calc_spectrum(data, N_fft):
    X_f = np.fft.fft(data, N_fft)
    X_f_shifted = np.fft.fftshift(X_f)

    return X_f_shifted
