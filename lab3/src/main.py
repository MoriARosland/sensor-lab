from preprocessing import txt_to_numpy_array
from fft import calc_and_plot_fft

N_FFT = 4096*2
Fs = 30  # 30 frames pr.second


def main():
    data = txt_to_numpy_array("lab3/data/okmaling.txt")

    calc_and_plot_fft(data[0])
    calc_and_plot_fft(data[1])
    calc_and_plot_fft(data[2])


if __name__ == "__main__":
    main()
