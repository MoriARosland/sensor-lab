import numpy as np


def calc_normalized_power_spectrum(data, N_fft):
    if (N_fft < len(data)):
        print("N_fft length to low. N_fft must be greater than legth of provided data.")
        exit(-1)
    if not np.log2(N_fft).is_integer():
        print(
            f"Data lenght is: {len(data)}. The closest power to your data lenght is: {round(2**(np.ceil(np.log2(len(data)))))}.\n"
        )
        print("Recommended N_ftt is 2^n")
        exit(-1)

    S_x = 20*np.log10(abs(data))  # Power in decibel
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


def generate_freq_array(F_s, N_fft):
    F_s = F_s / 2
    N_fft = N_fft // 2

    return np.linspace(0, F_s, N_fft)
