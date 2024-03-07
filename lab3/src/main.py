import os
import numpy as np
from preprocessing import txt_to_numpy_array
from postprocessing import calc_and_plot_fft, colorData_timeplot

START = 500
END = -1

COLORS = ["Red", "Green", "Blue"]


def main():
    path = "/Users/rosland/development/sensor-lab/lab3/data/hr_reflektans/"
    # path = "/Users/rosland/development/sensor-lab/lab3/data/hr_transmittans/one.txt"

    if os.path.isdir(path):
        for i in range(3):
            print(f'// --- Channel: {COLORS[i]} --- //')

            heart_rate = [
                calc_and_plot_fft(
                    txt_to_numpy_array(f"{path}{file}")[START:END, i], COLORS[i]
                )
                for file in os.listdir(path)
                if file != ".DS_Store"
            ]

            heart_rate = sorted(heart_rate)

            avg = round(np.mean(heart_rate), 2)
            std = round(np.std([abs(el) for el in heart_rate]), 4)

            print(f"Average HR: {avg}")
            print(f"Standard deviation from heart rates: {std}")
    else:
        data = txt_to_numpy_array(path)

        for i in range(3):
            calc_and_plot_fft(data[START:END, i], COLORS[i])
            colorData_timeplot(data[START:END, i], COLORS[i])


if __name__ == "__main__":
    main()
