# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:26:09 2015

@author: Lukas Gartmair
"""
import slidingwindows
import numpy as np

def calc_strainrate(slice_x, slice_y):
    sr = (float(slice_y[1]-slice_y[0])/(slice_x[1]-slice_x[0]))
    return sr

def make_slices(inp_array):
    slices = slidingwindows.sliding_window(inp_array,2,1)
    return slices

def calc_plast_strainrate_with_fit(time_corr, strain_plast):
    
    strainrate_plast = np.arange(0)
    time_slices = make_slices(time_corr)
    strain_slices = make_slices(strain_plast)
    for index,s in enumerate(strain_slices):
        sub_strainrate_plast = calc_strainrate(time_slices[index],s)
        strainrate_plast = np.hstack((strainrate_plast,sub_strainrate_plast))
    return strainrate_plast

# + time means    
    
def get_corresponding_means(strain_plast):

    strain_means = np.arange(0)
    strain_slices = make_slices(strain_plast) 
    strain_means = np.mean(strain_slices, axis = 1)
    return strain_means
    
import unittest

# for sclice options 2,1
ms_test_arr = np.arange(5)
ms_test_arr_res = np.array([[0,1],[1,2],[2,3],[3,4]])

cs_test_arr1_x = np.arange(2)
cs_test_arr1_y = np.array([2,2])
cs_test_arr1_res = 0

cs_test_arr2_x = np.arange(2)
cs_test_arr2_y = np.arange(2)
cs_test_arr2_res = 1

cs_test_arr3_x = np.array([2,4])
cs_test_arr3_y = np.array([10,30])
cs_test_arr3_res = 10

cm_test_arr = np.arange(5)
cm_test_arr_res = np.array([0.5,1.5,2.5,3.5])

class CalcPlastStrainRateTest(unittest.TestCase):

    def test_make_slices(self):
        np.testing.assert_array_equal(make_slices(ms_test_arr),ms_test_arr_res)
        
    def test_calc_strainrate(self):
        np.testing.assert_array_equal(calc_strainrate(cs_test_arr1_x, cs_test_arr1_y),cs_test_arr1_res)
        np.testing.assert_array_equal(calc_strainrate(cs_test_arr2_x, cs_test_arr2_y),cs_test_arr2_res)
        np.testing.assert_array_equal(calc_strainrate(cs_test_arr3_x, cs_test_arr3_y),cs_test_arr3_res)
        
    def test_get_corresponding_means(self):
        np.testing.assert_array_equal(get_corresponding_means(cm_test_arr), cm_test_arr_res)
        

def main():
    unittest.main()
if __name__ == '__main__':
    main()