import numpy as np
import random

# Solution to task 1 (preparation task)

SPEED_OF_SOUND = 343
ARRAY_SPACING = 0.1
Fs = 16000

SAMPLE_PERIOD = 1 / Fs

MAX_DELAY = ARRAY_SPACING / SPEED_OF_SOUND
MAX_LAG = round(MAX_DELAY / SAMPLE_PERIOD)

LAGS = np.arange(0, MAX_LAG + 1)
SIGNAL_DELAY = random.choice(LAGS)  # Delay in number of samples

f = 10
omega = 2 * np.pi * f

t = np.arange(0, 1, SAMPLE_PERIOD)
x = np.sin(omega * t)
y = np.roll(x, SIGNAL_DELAY)
y[:SIGNAL_DELAY] = 0  # Setting the rolled samples to 0


def normalized_cross_correlation(x, y, lags):
    result = np.zeros(len(lags))
    len_x = len(x)

    auto_corr_x = np.sum(x**2)
    auto_corr_y = np.sum(y**2)
    norm_factor = np.sqrt(auto_corr_x * auto_corr_y)

    for i, lag in enumerate(lags):
        lag_sum = 0

        for n in range(len_x - lag):
            lag_sum += x[n] * y[n + lag]

        result[i] = lag_sum
    return result / norm_factor


corr = np.abs(normalized_cross_correlation(x, y, LAGS))
max_corr_index = np.argmax(corr)  # Index of the maximum value in the correlation array
print(f"The signals have a maximum correlation when the lag is {max_corr_index} samples")
