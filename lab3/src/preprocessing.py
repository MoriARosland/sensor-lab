import numpy as np
from scipy.signal import detrend


def txt_to_numpy_array(txtdata_filepath):

    data = np.genfromtxt(txtdata_filepath, delimiter=" ")
    # data = np.transpose(data)

    return data
