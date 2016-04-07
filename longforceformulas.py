# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 01:32:39 2015

@author: Lukas Gartmair
"""

import linfit
import numpy as np

def get_linregs_of_long_force(longitudination_orig, force, trans_index):

    pivot_long = [l for l in longitudination_orig[0:trans_index+1]]
    pivot_force = [f for f in force[0:trans_index+1]]

    m = linfit.linfit(pivot_long, pivot_force)[0][0]
    t = linfit.linfit(pivot_long, pivot_force)[0][1]

    return m, t


def correct_longitudination(longitudination_orig, m, t):

    # triangle m = t/x
    # -> x = t/m and a right shift thorugh zero
    shift = t / m
    longitudination_corr = np.arange(0)
    longitudination_corr = longitudination_orig + shift
    return longitudination_corr
