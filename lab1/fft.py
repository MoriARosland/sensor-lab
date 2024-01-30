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
