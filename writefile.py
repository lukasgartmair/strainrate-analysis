# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:53:32 2015

@author: Lukas Gartmair
"""

import numpy as np

def summarize(*args):    
    summary = np.array(args)
    return summary

def write_summary(summary):
    filename = 'summary.txt'
    np.savetxt(filename, np.transpose([summary]), header= 'Datapoint Nr., Time / s, Strain plast / %, Strainrate plast / %/s, Strain True / %, Stress True / MPa, Filtered Strain plast / %, Filtered Strainrate plast / %/s', delimiter=',', comments = '')

