from preprocessing import txt_to_numpy_array
from fft import calc_and_plot_fft, color_time_plot

N_FFT = 4096*2
Fs = 30  # 30 frames pr.second


def main():
    data = txt_to_numpy_array("lab3/data/hr_data/close5.txt")

    # calc_and_plot_fft(data[0])
    # calc_and_plot_fft(data[1])
    # calc_and_plot_fft(data[2])

    color_time_plot(data[0])
    color_time_plot(data[1])
    color_time_plot(data[2])


if __name__ == "__main__":
    main()
