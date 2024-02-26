import numpy as np
from scipy.signal import detrend


def calc_angle(n12, n13, n23):
    numerator = np.sqrt(3) + n12 + n13
    denumenator = n12 - n13 - 2 * n23

    angle = np.arctan(numerator / denumenator)

    if denumenator < 0:
        angle += np.pi

    return angle


def estimate_angle(sample_period, data):
    sample_start = 10000
    sample_end = 15000

    for i in range(0, 3):
        data[:, i] = detrend(data[:, i])

    # Adjust just index to the corresponding microphone.
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

    for i in range(3):
        sound[i] = np.interp(x_vals, x, sound[i])

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
        # index of max value
        max_index = np.argmax(np.abs(corr[i]))
        delay = l[max_index]
        lags[list(lags.keys())[i]] = delay

        # plt.plot(l, corr[i])
        # plt.title(f"Correlation \nLag: {delay}")
        # plt.xlabel("Lag")
        # plt.ylabel("Amplitude")
        # plt.show()

    angle = calc_angle(**lags)

    angle = 180 * angle / np.pi

    if angle > 180:
        angle -= 360

    return round(angle * 1000) / 1000
