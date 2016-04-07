# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:15:48 2015

@author: Lukas
"""

import linfit
import numpy as np

def add_last_value(strainrate_plast_filtered_log, strain_plast_means_filtered, strain_plast):

    # n defines the extrapolation section backwards
    n = 3

    X = strain_plast_means_filtered[-n:]
    Y = strainrate_plast_filtered_log[-n:]

    m = linfit.linfit(X, Y)[0][0]
    t = linfit.linfit(X, Y)[0][1]

    extrapolated_sr = np.power((m * strain_plast[-1] + t),10)

    np.append(strainrate_plast_filtered_log,extrapolated_sr)

    np.append(strain_plast_means_filtered,strain_plast[-1])

