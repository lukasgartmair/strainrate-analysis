# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:25:06 2015

@author: Lukas Gartmair
"""
from numpy import loadtxt

def load_txt(filepath):
    # skip header 
    t,l,f = loadtxt(filepath,skiprows = 1, usecols = (0,1,2),unpack = True)
    return t,l,f
    