import linfit
import numpy as np

# slope(x) = f(x)-f(x-1)
# slope2(x) = slope(x) - slope(x-1)

def slopedec(X, Y, window_fraction):
    ### calculates changes in slope ###
    slopes1 = []
    slopes2 = []
    for (pos, x) in enumerate(X):
        slope1 = 0
        if pos < len(X) - window_fraction:
            slope1 = linfit.linfit(
                X[pos:pos + window_fraction], Y[pos:pos + window_fraction])[0][0]
            slopes1.append(slope1)
    for (pos, slope1) in enumerate(slopes1):
        if pos >= 1 and pos < len(slopes1):
            slope2 = 0
            slope2 = slopes1[pos] - slopes1[pos - 1]
            slopes2.append(slope2)
    nd_slopes2 =  np.asarray(slopes2)
    return nd_slopes2

# nice to know in this context
# answered Nov 22 '12 at 4:59
#BrenBarn
#Unlike the list append method, numpy's append does not append in-place. It returns a new array with the extra elements appended. 
#So you'd need to do r = np.append(r, float(line[index])).
#
#Building up numpy arrays in this way is inefficient, though. 
#It's better to just build your list as a Python list and then make a numpy array at the end.

import unittest

# set up the test cases
window_fraction = 5
sd_X_unittest = np.arange(30)
sd_Y_unittest_all_zero = np.array([y*2 for y in range(30)])
sd_Y_unittest_middlepeak = np.copy(sd_Y_unittest_all_zero)
sd_Y_unittest_middlepeak[15] = 100

sd_test_result_all_zero = np.array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
sd_test_result_middlepeak = np.array([  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,  14.,
        -7.,  -7.,  -7.,  -7.,  14.,   0.,   0.,   0.,   0.,   0.,   0.,
         0.,   0.])

class SlopeDetectionTest(unittest.TestCase):

    def test_slopedec(self):
        np.testing.assert_array_equal(slopedec(sd_X_unittest,sd_Y_unittest_all_zero, window_fraction),sd_test_result_all_zero )
        np.testing.assert_array_equal(slopedec(sd_X_unittest,sd_Y_unittest_middlepeak, window_fraction),sd_test_result_middlepeak )
def main():
    unittest.main()
if __name__ == '__main__':
    main()
