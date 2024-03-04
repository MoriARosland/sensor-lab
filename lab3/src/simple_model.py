import numpy as np
from tabulate import tabulate


muabo = np.genfromtxt("lab3/data/txt/muabo.txt", delimiter=",")
muabd = np.genfromtxt("lab3/data/txt/muabd.txt", delimiter=",")

# Wavelengths where color channel sensitivity is highest (determined by camera type)
red_wavelength = 600
green_wavelength = 515
blue_wavelength = 460

wavelength = np.array([red_wavelength, green_wavelength, blue_wavelength])


def mua_blood_oxy(x): return np.interp(x, muabo[:, 0], muabo[:, 1])
def mua_blood_deoxy(x): return np.interp(x, muabd[:, 0], muabd[:, 1])


bvf = 0.01  # Blood volume fraction, average blood amount in tissue
oxy = 0.8  # Blood oxygenation

# Absorption coefficient ($\mu_a$ in lab text)
# Units: 1/m
mua_other = 25  # Background absorption due to collagen, et cetera
mua_blood = (mua_blood_oxy(wavelength)*oxy  # Absorption due to
             + mua_blood_deoxy(wavelength)*(1-oxy))  # pure blood
mua = mua_blood*bvf + mua_other

# reduced scattering coefficient ($\mu_s^\prime$ in lab text)
# the numerical constants are thanks to N. Bashkatov, E. A. Genina and
# V. V. Tuchin. Optical properties of skin, subcutaneous and muscle
# tissues: A review. In: J. Innov. Opt. Health Sci., 4(1):9-38, 2011.
# Units: 1/m
musr = 100 * (17.6*(wavelength/500)**-4 + 18.78*(wavelength/500)**-0.22)

# mua and musr are now available as shape (3,) arrays
# Red, green and blue correspond to indexes 0, 1 and 2, respectively


# Solution task 1a

skin_depth = np.sqrt(1/(3*(musr + mua)*mua))

coefficients = [["Absorption coefficient (Red)", mua[0]],
                ["Absorption coefficient (Green)", mua[1]],
                ["Absorption coefficient (Blue)", mua[2]],
                ["Reduced scattering coefficient (Red)", musr[0]],
                ["Reduced scattering coefficient (Green)", musr[1]],
                ["Reduced scattering coefficient (Blue)", musr[2]]]

print(tabulate(coefficients, headers=["Coefficient", "Value"], tablefmt="grid"))
penetration_depth = [["Red", skin_depth[0]],
                     ["Green", skin_depth[1]],
                     ["Blue", skin_depth[2]]]

print(tabulate(penetration_depth, headers=["Color", "Penetration Depth"], tablefmt="grid"))


# Solution task 1b

FINGER_THICKNESS = 1.2 * 10**-2  # Meters


def calc_transmittance(fingerThickness, mua, musr):

    transmittances = np.zeros(3)

    for i in range(3):
        C = np.sqrt(3*mua[i]*(musr[i]+mua[i]))
        transmittances[i] = np.exp(-C*fingerThickness)

    return transmittances


transmittance = calc_transmittance(FINGER_THICKNESS, mua, musr)

results = [["Color", "Transmittance through 1.2 cm finger"],
           ["Red", transmittance[0]],
           ["Green", transmittance[1]],
           ["Blue", transmittance[2]]]

print(tabulate(results, headers="firstrow", tablefmt="grid"))


# Solution task 1c

def calc_reflectance(mua, musr):

    reflectances = np.zeros(3)

    for i in range(3):
        reflectances[i] = np.sqrt(3*(musr[i]/mua[i]+1))

    return reflectances


reflectance = calc_reflectance(mua, musr)
relative_reflectance = np.zeros((3, 3))

relative_reflectance[0, 0] = reflectance[0] / reflectance[0]
relative_reflectance[0, 1] = reflectance[0] / reflectance[1]
relative_reflectance[0, 2] = reflectance[0] / reflectance[2]
relative_reflectance[1, 0] = reflectance[1] / reflectance[0]
relative_reflectance[1, 1] = reflectance[1] / reflectance[1]
relative_reflectance[1, 2] = reflectance[1] / reflectance[2]
relative_reflectance[2, 0] = reflectance[2] / reflectance[0]
relative_reflectance[2, 1] = reflectance[2] / reflectance[1]
relative_reflectance[2, 2] = reflectance[2] / reflectance[2]

results = [["Color", "Reflectance", "Relative Reflectance (Red)", "Relative Reflectance (Green)", "Relative Reflectance (Blue)"],
           ["Red", reflectance[0], relative_reflectance[0, 0], relative_reflectance[0, 1], relative_reflectance[0, 2]],
           ["Green", reflectance[1], relative_reflectance[1, 0], relative_reflectance[1, 1], relative_reflectance[1, 2]],
           ["Blue", reflectance[2], relative_reflectance[2, 0], relative_reflectance[2, 1], relative_reflectance[2, 2]]

           ]

print(tabulate(results, headers="firstrow", tablefmt="grid"))
