import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend


def calc_angle(n12, n13, n23):
    numerator = np.sqrt(3) * (n12 + n13)
    denumenator = n12 - n13 - 2 * n23

    angle = np.arctan(numerator / denumenator)

    if denumenator < 0:
        angle += np.pi

    return angle


def estimate_angle(sample_period, data):
    sample_start = 10000  # Vicinitty of clap
    sample_end = 15000

    for i in range(2, 5):
        data[:, i] = detrend(data[:, i])

    sound = [
        data[sample_start:sample_end, 4],
        data[sample_start:sample_end, 2],
        data[sample_start:sample_end, 3],
    ]

    interpolation_factor = 8

    x = np.arange(0, len(sound[0]) * sample_period, sample_period)
    x_vals = np.arange(
        0, len(sound[0]) * sample_period, sample_period / interpolation_factor
    )

    # _, ax = plt.subplots(2)
    # ax[0].plot(x[:50], sound[0][:50], marker=".")

    for i in range(3):
        sound[i] = np.interp(x_vals, x, sound[i])

    # ax[1].plot(x_vals[:100], sound[0][:100], marker=".")
    # plt.show()

    corr = [
        np.correlate(sound[1], sound[0], "full"),
        np.correlate(sound[2], sound[0], "full"),
        np.correlate(sound[2], sound[1], "full"),
    ]

    lags = {
        "n12": 0,
        "n13": 0,
        "n23": 0,
    }

    num_samples = len(sound[0])
    l = np.arange(-num_samples + 1, num_samples)

    for i in range(3):
        max_index = np.argmax(np.abs(corr[i]))
        delay = l[max_index]
        lags[list(lags.keys())[i]] = delay

        # plt.plot(l, corr[i])

        # plt.title(f"Correlation \nLag: {delay}")
        # plt.xlabel("Lag")
        # plt.ylabel("Amplitude")

        # plt.show()

    # autocorr = np.correlate(sound[0], sound[0], "full")
    # max_index = np.argmax(np.abs(autocorr))
    # delay = l[max_index]
    # lags["n11"] = delay

    # Plot the autocorr in the same manner as the crosscorr
    # plt.plot(l, autocorr)
    # plt.title(f"Autocorrelation \nLag: {delay}")
    # plt.xlabel("Lag")
    # plt.ylabel("Amplitude")
    # plt.show()

    angle = calc_angle(**lags)

    angle = 180 * angle / np.pi

    if angle > 180:
        angle -= 360

    return round(angle * 1000) / 1000
