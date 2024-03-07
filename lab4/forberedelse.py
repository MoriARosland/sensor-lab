import numpy as np

# Radar data sheet: https://rfbeam.ch/wp-content/uploads/dlm_uploads/2022/11/K-LC6_Datasheet.pdf

# ------- Oppg 9.1 ------- #
# 1. Beregn teoretisk dopplerskift som funksjon av radiell hastighet ved 24.13 GHz senterfrekvens.
c = 300000000  # m/s
f_0 = 24.13 * 10**9  # Hz


def calculate_doppler_shift(v_r):
    return 2*f_0*v_r/c


# 2. Beregn antennevinning ut fra ligning (III.7) og sammenlign med data som fins i databladet for radaren.


def calculate_antenna_gain(phi_azimuth, phi_elevation):
    return 10 * np.log10(30000/(phi_azimuth*phi_elevation))  # returns in dBi


azimuth = 12  # degrees
elevation = 80

G = round(calculate_antenna_gain(azimuth, elevation), 2)  # dBi
G_data_sheet = 12.5  # dBi
G_diff = round(G - G_data_sheet, 3)

print(f"Antenna gain: {G} dB")
print(f"Deviation from data sheet: {G_diff} dB")

# 3. Beregn radartverrsnittet ved 24 GHz til en hjørnereflektor som har sidekant a = 21 cm.
wavelength = c/f_0


def calculate_radar_cross_section(a):
    return (4 * np.pi * a**4) / (3*wavelength**2)


a = 21*10**-2  # m
a_radar = round(calculate_radar_cross_section(a), 3)

print(f"Radar cross section: {a_radar} m^2")


# 4. Hvor mye må reflektoren beveges radielt for at I-Q-phasoren skal foreta et 360-graders faseomløp?

# phi = 2*pi = 2*pi*2*distance/ wave_length (eq.1, from lecture slides)
# Solve eq.1 for distance => distance = wave_length / 2

def calculate_radial_movement(wave_length):
    return wave_length / 2


displacement_distance = round(calculate_radial_movement(wavelength), 3)
print(
    f"The reflected wave experiences a 360 deg phase-shift when displaced by pluss/minus {displacement_distance} m")
