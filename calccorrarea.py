# the correct area has to be calculated from the initial area
# the thermal coefficient and the delta in temperature

# iapws 1.1.1 should work better     alfav, Thermal expansion coefficient
# (Volume expansivity), 1/K


def calc_area_corr(temperature, initial_area, thermal_expansion_coeff):

    RT = 298  # K
    delta_T = temperature - RT
    area_corr = initial_area * \
        ((1 + ((thermal_expansion_coeff * delta_T)**2)))  # mm**2

    return area_corr

## unittest

import unittest

# set up

thermal_expansion_coeff1 = 2e-5 # 1/K
thermal_expansion_coeff2 = 1e-5 # 1/K
thermal_expansion_coeff3 = 0 # 1/K
temperature1 = 298 # K
temperature2 = 1298 # K
temperature3 = 2298 # K

initial_area = 5

# Here's our "unit tests".
class CalcCorrAreaTest(unittest.TestCase):
    
    def test_calc_corr_area_temp(self):
        self.assertEqual(calc_area_corr(temperature1, initial_area, thermal_expansion_coeff1),5)
        self.assertEqual(calc_area_corr(temperature2, initial_area, thermal_expansion_coeff1),5.002)
        self.assertEqual(calc_area_corr(temperature3, initial_area, thermal_expansion_coeff1),5.008)
    def test_calc_corr_area_tec(self):
        self.assertEqual(calc_area_corr(temperature3, initial_area, thermal_expansion_coeff1),5.008)
        self.assertEqual(calc_area_corr(temperature3, initial_area, thermal_expansion_coeff2),5.002)
        self.assertEqual(calc_area_corr(temperature3, initial_area, thermal_expansion_coeff3),5)

def main():
    unittest.main()

if __name__ == '__main__':
    main()