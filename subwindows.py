# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:04:23 2015

@author: Lukas Gartmair
"""
import slidingwindows

def sub_windows(time_corr, strain_plast, window_size):
    
    windows_t = slidingwindows.sliding_window(time_corr,window_size,ss = None,flatten = False)
    windows_st = slidingwindows.sliding_window(strain_plast,window_size,ss = None,flatten = False)
    
    return windows_t, windows_st