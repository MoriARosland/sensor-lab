import numpy as np
from scipy.signal import detrend


def txt_to_numpy_array(txtdata_filepath):

    data = np.loadtxt(txtdata_filepath)
    dataTransposed = np.transpose(data)

    # Indexing: Red, Green, Blue
    return dataTransposed
