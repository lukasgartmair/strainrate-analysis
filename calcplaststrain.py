import numpy as np

def calc_plast_strain(strain_true, stress_true, slope_elast):

    plast_strain = np.arange(0)
    plast_strain = strain_true - (stress_true/slope_elast)

    return plast_strain
