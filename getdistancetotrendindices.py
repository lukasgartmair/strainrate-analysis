# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:05:50 2015

@author: Lukas Gartmair
"""

import numpy as np

def get_distance_to_trend_indices(m_sub, t_sub, pivot_strain):
    # y = mx + t
    distances = np.arange(0)
    indices = np.arange(0)
    y_trends = np.arange(0)
    distances = np.arange(0)
    
    y_trends = (m_sub * pivot_strain) + t_sub
    distances = np.absolute(y_trends - pivot_strain)

    indices = np.argsort(distances)
    return indices