# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:56:11 2016

@author: Lukas Gartmair
"""

import numpy as np
import matplotlib.pyplot as pl

import csv

def get_header():
    header = ['strain_plast_means_orig', 'strainrate_plast_orig',
              'strain_plast_filtered', 'strainrate_plast_filtered',
              'time_corr', 'strain_true', 'stress_true']
    return header
    
def write_summary(*args):
    rows = zip(np.transpose(args))
    b = open('summary.txt', 'w')
    writer = csv.writer(b)
    header = get_header()
    writer.writerow(header)
    for x,row in enumerate(rows):
        writer.writerow(row[0])
    b.close()

#test

x = np.array([1,2,3])
y = np.array([5,6,7])
z = np.array([6,9,7])

write_summary(x,y,z)