# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:33:59 2015

@author: Lukas Gartmair
"""

import numpy as np

def get_clostest_points_to_trend(nopts, ranked_indices, time_corr, strain_plast):

    sub_time_filtered = np.take(time_corr,ranked_indices[0:nopts])
    sub_strain_plast_filtered = np.take(strain_plast,ranked_indices[0:nopts])
    
    return sub_time_filtered, sub_strain_plast_filtered
