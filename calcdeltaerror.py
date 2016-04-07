# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:11:15 2015

@author: Lukas Gartmair
"""

import matplotlib.pyplot as pl

def calc_delta_error(window_fitparas, window_errors):
    
    # number of windows
    now = [w+1 for w in range(len(window_errors))]
    
    ms = [w[0] for w in window_fitparas]
    ts = [w[1] for w in window_fitparas]    
    dms = [w[0] for w in window_errors]
    dts = [w[1] for w in window_errors]
     
    ###################################

    fig = pl.figure()
    #pl.errorbar(ms, xerr=dms, yerr=dts)
    pl.errorbar(now, ms, yerr=dms, color = 'red',  fmt='o')
    pl.xlabel('window number')
    pl.ylabel('m + error(dm)')
    fig = pl.figure()
    pl.errorbar(now, ts, yerr=dts, color = 'blue',  fmt='o')
    
#    pl.plot(dms, color ='blue')
#    pl.plot(dts, color = 'red')
#    ymin = min(dts)
#    ymax = max(dts)
    pl.xlabel('window number')
    pl.ylabel('t + error(dt)')
#    
#    #######################################
