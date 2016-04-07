def calc_height_corr(temperature, initial_height, thermal_expansion_coeff):

    RT = 298  # K
    delta_T = temperature - RT
    height_corr = initial_height * \
        ((1 + ((thermal_expansion_coeff * delta_T)**2)))  # mm

    return height_corr

## unittest

import unittest

# set up

thermal_expansion_coeff1 = 2e-5 # 1/K
thermal_expansion_coeff2 = 1e-5 # 1/K
thermal_expansion_coeff3 = 0 # 1/K
temperature1 = 298 # K
temperature2 = 1298 # K
temperature3 = 2298 # K

initial_height = 5 # mm**2

# Here's our "unit tests".
class CalcCorrHeightTest(unittest.TestCase):
    
    def test_calc_corr_height_temp(self):
        self.assertEqual(calc_height_corr(temperature1, initial_height, thermal_expansion_coeff1),5)
        self.assertEqual(calc_height_corr(temperature2, initial_height, thermal_expansion_coeff1),5.002)
        self.assertEqual(calc_height_corr(temperature3, initial_height, thermal_expansion_coeff1),5.008)
    def test_calc_corr_height_tec(self):
        self.assertEqual(calc_height_corr(temperature3, initial_height, thermal_expansion_coeff1),5.008)
        self.assertEqual(calc_height_corr(temperature3, initial_height, thermal_expansion_coeff2),5.002)
        self.assertEqual(calc_height_corr(temperature3, initial_height, thermal_expansion_coeff3),5)

def main():
    unittest.main()

if __name__ == '__main__':
    main()