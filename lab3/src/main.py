from preprocessing import txt_to_numpy_array
from fft import calc_and_plot_fft, colorData_timeplot


def main():
    data = txt_to_numpy_array("lab3/data/hr_data/close4.txt")

    calc_and_plot_fft(data[0])
    calc_and_plot_fft(data[1])
    calc_and_plot_fft(data[2])

    colorData_timeplot(data[0])
    colorData_timeplot(data[1])
    colorData_timeplot(data[2])


if __name__ == "__main__":
    main()
