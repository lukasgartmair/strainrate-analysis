# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:42:25 2015

@author: Lukas
"""
import matplotlib.pyplot as pl
import numpy as np

def plot(save_path, X, Y, color_line, title, bool_filtered):

    fig = pl.figure()

    if bool_filtered == True:
        pl.scatter(X[:], Y[:], color=color_line)
        pl.title("Filtered Data")
    else:
        pl.scatter(X, Y, color=color_line)
        pl.title("Unfiltered Data")

    pl.xlabel('time / s')
    pl.ylabel('strain / %')

    pl.grid()

    plot_path = (save_path + '_' + str(title) + '.png')

    fig.savefig(plot_path)

    return plot_path

def plot_log(save_path, X, Y, color_line, title, bool_filtered):
    fig = pl.figure()

    if bool_filtered == True:
        pl.scatter(X[:-1], Y[:-1], color=color_line, label='normal')
        pl.scatter(X[-1], Y[-1], color='red', label='extrapolated')
        pl.title("Filtered Data with last point extrapolated")
    else:
        pl.scatter(X, Y, color=color_line)
        pl.title("Unfiltered Data")

    pl.xlabel('strain / %')
    pl.ylabel('strainrate / %/s')

    pl.yscale('log')

    ymin = np.amin(np.absolute(Y)) * 1e-1
    ymax = np.amax(np.absolute(Y)) * 1e1

    pl.ylim((ymin, ymax))
    pl.grid()

    if bool_filtered == True:
        pl.legend()

    plot_path = (save_path + '_' + str(title) + '.png')
    fig.savefig(plot_path)

    # plt.show()

    return plot_path

def plot_setup(save_path, time_corr_filtered, strain_plast_filtered, strain_plast_means_filtered, strainrate_plast_filtered, strain_plast, time_corr, strain_plast_means_orig, strainrate_plast_orig):
    ## PLOTTING ###
    # strain / time
    plotpath_filtered_st_tc = plot(
        save_path, time_corr_filtered, strain_plast_filtered, 'red', 'filtered data_strain_time', True)

    plotpath_original_st_tc = plot(
        save_path, time_corr, strain_plast, 'red', 'original data_strain_time', False)

    # strainrates
    plotpath_filtered = plot_log(
        save_path, strain_plast_means_filtered, strainrate_plast_filtered, 'blue', 'filtered data', True)

    plot_path_original = plot_log(
        save_path, strain_plast_means_orig, strainrate_plast_orig, 'blue', 'original data', False)
        
    return plotpath_filtered_st_tc, plotpath_original_st_tc,  plotpath_filtered, plot_path_original

