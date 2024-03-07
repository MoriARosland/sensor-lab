import os
import numpy as np
from preprocessing import txt_to_numpy_array
from fft import calc_and_plot_fft, colorData_timeplot

START = 500
END = -1


def main():
    data = txt_to_numpy_array("/Users/rosland/Documents/sensor-lab/lab-3/data/reflektans/four.txt")
    # data = txt_to_numpy_array("lab3/data/hr_data/Transmittans-2.txt")

    # calc_and_plot_fft(data[START:END, 0])
    # calc_and_plot_fft(data[START:END, 1])
    # calc_and_plot_fft(data[START:END, 2])

    # colorData_timeplot(data[START:END, 0])
    # colorData_timeplot(data[START:END, 1])
    # colorData_timeplot(data[START:END, 2])

    path = "/Users/rosland/development/sensor-lab/lab3/data/hr_reflektans/"
    path = "/Users/rosland/development/sensor-lab/lab3/data/hr_transmittans/"

    for i in range(3):
        pulses = [
            calc_and_plot_fft(
                txt_to_numpy_array(f"{path}{file}")[START:END, i]
            )
            for file in os.listdir(path)
            if file != ".DS_Store"
        ]

        pulses = sorted(pulses)

        avg = round(np.mean(pulses), 2)
        print(f"Average pulse:{avg}")

        std = round(np.std([abs(el) for el in pulses]), 4)
        print(f"Standard deviation from pulses:{std}")


if __name__ == "__main__":
    main()
