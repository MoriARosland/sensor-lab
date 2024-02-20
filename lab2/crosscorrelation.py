import numpy as np

# Solution to task 1 (forberedelse)

SPEED_OF_SOUND = 343
ARRAY_SPACING = 0.1
Fs = 16000

SAMPLE_PERIOD = 1 / Fs

MAX_DELAY = ARRAY_SPACING / SPEED_OF_SOUND
MAX_LAG = round(MAX_DELAY / SAMPLE_PERIOD)

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 2, 4, 5])
lags = np.arange(-MAX_LAG, MAX_LAG + 1)


def crosscorrelation(x, y, lags):
    corr_values = [np.correlate(x, np.roll(y, lag), mode='full') for lag in lags]
    return np.array(corr_values)


# Compute cross-correlation for all lags
corr_values = crosscorrelation(x, y, lags)

# Find the absolute maximum of the cross-correlation values
max_corr_value = np.max(np.abs(corr_values))

print("The absolute value of the largest cross-correlation is:", max_corr_value)
