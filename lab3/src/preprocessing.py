import numpy as np
from scipy.signal import detrend


def txt_to_numpy_array(txtdata_filepath):

    data = np.loadtxt(txtdata_filepath)
    dataTransposed = np.transpose(data)

    for i in range(len(dataTransposed)):
        dataTransposed[i] = detrend(dataTransposed[i])

    # Indexing: Red, Green, Blue
    return dataTransposed
