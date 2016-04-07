# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:28:31 2016

@author: fe63vimy
"""
import numpy as np

# filter parameter is the minimum distance between two array indices
# this step is done in oder to let only minimum 3 points in the function linfit



def get_indices_to_keep(arr):
    
    # linfit requires 3 input arguments
    filter_parameter = 3
    
    indices_to_keep = []
    counter = 0
    for x in range(arr.size):
        if x < counter:
            continue
        elif x>= counter:
            summe = 0
            for y in range(arr.size):
                if y > x:
                    # important take only the differene between them
                    summe += (arr[y]-arr[x])
                    if summe > filter_parameter:
                        indices_to_keep.append(y)
                        counter = y
                        break

    filtered_arr = np.arange(0)
    filtered_arr = np.take(arr,indices_to_keep)

    return filtered_arr
                        

def get_ratio_dependent_windows(strain_plast, slope_ratios):
    window_indices1 = np.arange(0)
    # get every index where a window change should happen
    lower_limit = 0.9
    upper_limit = 1.1    
    
    window_indices1_below = (np.where(slope_ratios < lower_limit))[0]
    window_indices1_above = (np.where(slope_ratios > upper_limit))[0]
    window_indices1 = np.concatenate((window_indices1_below,window_indices1_above),0)
    return  window_indices1

def get_strain_dependent_windows(strain_plast, slope_ratios, strain_window_size):
    
    window_indices2 = []
    # strain dependent window control
    strain_total = max(strain_plast) -  min(strain_plast)
    strain_window_size = round(strain_total / strain_window_size,4)
    # but in every case create a new window every x percent % strain
    current_strain_window = strain_window_size + min(strain_plast)
    for x in range(len(strain_plast)):
        if  strain_plast[x] >= current_strain_window:
            window_indices2.append(x)  
            current_strain_window += strain_window_size
    return np.asarray(window_indices2)


def split_windows(slope_ratios, time_corr, strain_plast, strain_window_size):
    # ratio dependent window sizes
    window_indices1  = get_ratio_dependent_windows(strain_plast, slope_ratios)
    # strain interval dependent window sizes
    window_indices2 = get_strain_dependent_windows(strain_plast, slope_ratios, strain_window_size)
    window_indices = np.concatenate((window_indices1, window_indices2),0)
    window_indices = np.unique(window_indices)
    window_indices = np.sort(window_indices, axis=-1, kind='quicksort', order=None)
    print('window_indices: ' + str(window_indices))
    print('window indices.size = ' + str(window_indices.size))
    window_indices_corr = get_indices_to_keep(window_indices)
    print('window_indices_corr: ' + str(window_indices_corr))

    time_corr_splitted = np.split(time_corr,window_indices_corr)
    strain_plast_splitted = np.split(strain_plast,window_indices_corr)
    
    return time_corr_splitted, strain_plast_splitted
    
import unittest

# for filter parameter == 3

test_array = np.array([0,1,2,3,4,5,6])
test_array_res = np.array([3,6])
test_array1 = np.array([  0,   1,   2,   3,   4,   6,   7,   8,   9,  13,  18,  23,  28,
        32,  38,  55,  75,  94, 110, 126, 142, 156, 168, 179]) 
test_array1_res = np.array([  3,   6,   9,  13,  18,  23,  28,  32,  38,  55,  75,  94, 110,
       126, 142, 156, 168, 179])

test_array2 = np.arange(20)
test_array2_res = np.array([3,6,9,12,15,18])

class IndicesToKeepTest(unittest.TestCase):
    
    def test_indices_to_keep(self):
        np.testing.assert_array_equal(get_indices_to_keep(test_array),test_array_res)
        np.testing.assert_array_equal(get_indices_to_keep(test_array1),test_array1_res)
        np.testing.assert_array_equal(get_indices_to_keep(test_array2),test_array2_res)
 
    
def main():
    unittest.main()
if __name__ == '__main__':
    main()