# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 01:24:16 2015

@author: Lukas Gartmair
"""

def correction_with_corr_value(l,f,t, corr_value):
    
    l_c = l[corr_value:]
    f_c = f[corr_value:]
    t_c = t[corr_value:]
    
    return l_c, f_c, t_c
