import numpy as np


def calc_strain_true(longitudination_corr, height):
    # log alone is naturalis as doc. says
    strain_true = np.arange(0)
    strain_true = -(np.log(1 + (longitudination_corr / height)))
    return strain_true


def calc_stress_true(force_corr, longitudination_corr, height, area):

    stress_true = np.arange(0)
    stress_true = (-(force_corr / area) *
             (1 + (longitudination_corr / height)))
    return stress_true


import unittest

# set up the test cases
ut_longitudination_corr = np.array([1,2,3,4,5,6,7,8,9,10])
ut_height = 10
ut_strain_res = np.array([-0.09531018, -0.18232156, -0.26236426, -0.33647224, -0.40546511,
       -0.47000363, -0.53062825, -0.58778666, -0.64185389, -0.69314718])
       
class CalcStrainStressTest(unittest.TestCase):

    def test_calc_strain_true(self):
        np.testing.assert_array_almost_equal(calc_strain_true(ut_longitudination_corr, ut_height), ut_strain_res)

def main():
    unittest.main()
if __name__ == '__main__':
    main()