from preprocessing import txt_to_numpy_array
from fft import plot_spectrum

N_FFT = 4096*2
Fs = 30  # 30 frames pr.second


def main():
    data = txt_to_numpy_array("lab3/data/okmaling.txt")

    plot_spectrum(data[0], N_FFT, Fs)


if __name__ == "__main__":
    main()
