import numpy as np
import sys
import os

from raspi_import import raspi_import
from triangulation import estimate_angle

# Credit to Aasmund Nørsett for angle estimation.


def main():
    # path = "/Users/rosland/development/sensor-lab/lab2/data/-90deg/"
    # path = "/Users/rosland/development/sensor-lab/lab2/data/0deg/"
    path = "/Users/rosland/development/sensor-lab/lab2/data/180deg/"

    if not os.path.isdir(path):
        sample_period, data = raspi_import(path)
        angle = estimate_angle(sample_period, data)
        print(angle)

        sys.exit(1)

    angles = [
        estimate_angle(*raspi_import(path + file))
        for file in os.listdir(path)
        if file != ".DS_Store"
    ]

    angles = sorted(angles, key=float)

    std = np.std([abs(el) for el in angles])

    print(angles)
    print(f"STD: {std}")
    print(f"Variance: {std**2}")


if __name__ == "__main__":
    main()
