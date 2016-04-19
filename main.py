# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:17:00 2015

@author: Lukas Gartmair
"""

import matplotlib.pyplot as pl

import numpy as np

import getpath
import loadtxt
import calccorrarea
import calccorrheight
import checkforshitinthebeginning
import longforceformulas
import correction
import calcstrainstress
import getslopeelast
import calcplaststrain
import filterdata
import calcdeltaerror
import calcplaststrainrate
import addlastvalue
import plot
import writefile

# filepath operations
filepath = ''
filepath = getpath.get_path()
save_path = filepath

# initialization
time_orig = np.array(np.arange(0))
longitudination_orig = np.array(np.arange(0))
force = np.array(np.arange(0))
# read in the columns
time_orig,longitudination_orig,force = loadtxt.load_txt(filepath)

# für schergos daten nur force *-1!
#longitudination_orig *= -1
#force *= -1

# corrections of area and height
temperature = 1298 #K
thermal_expansion_coeff = 2e-5 # 1/K
initial_height = 5 # mm
initial_area = 10 #mm
height = calccorrheight.calc_height_corr(
    temperature, initial_height, thermal_expansion_coeff)
area = calccorrarea.calc_area_corr(
    temperature, initial_area, thermal_expansion_coeff)
    
# filter parameters 
# number of points to store
nopts = 1
# window size for the slope dependent selection
slope_window_size = 5
# every nth strainfraction a new window has to take place
strain_window_size = 10

# bool delta error calculation 
bool_cde = True

#####################################################
########### ANALYSIS ################################

# correction

# check for equal values and then cut the first values
nonequal = checkforshitinthebeginning.check_for_equals_in_the_beginning(
    longitudination_orig)
print('nonequal: ' +str(nonequal))
# cut the first values- they are unimportant
longitudination_equal_corr, force_equal_corr, time_equal_corr = correction.correction_with_corr_value(longitudination_orig,force, time_orig, nonequal)

median = np.median(force_equal_corr)
tresh = 0.95*median
quantil = 0.2

transition_indices = np.where(force_equal_corr[:int(quantil*force_equal_corr.size)]>tresh)
# and the indices must lie in the first quantil
transition = transition_indices[0].size
print('elastic plastic transition index: ' + str(transition))

#### 
# trans index < 2 will raise an error
# raise error and let the user put in the youngs modul by hand
if transition < 2:
    transition = 2
#### 

m,t = longforceformulas.get_linregs_of_long_force(
    longitudination_equal_corr, force_equal_corr, transition)
    
print('m long-force: ' + str(m))
print('t long-force: ' + str(t))
longitudination_corr_tmp = longforceformulas.correct_longitudination(
    longitudination_equal_corr, m, t)

# correct everything refering the constant stress level
#longitudination_corr, force_corr,  time_corr = correction.correction_with_corr_value(longitudination_zero_corr, force_zero_corr, time_zero_corr,constant_stress_level)

# tmp just renaming
longitudination_corr = longitudination_corr_tmp
force_corr = force_equal_corr
time_corr = time_equal_corr

### 2nd step ###
# calculate strain true and stress true

strain_true = calcstrainstress.calc_strain_true(
    longitudination_corr, height)
stress_true = calcstrainstress.calc_stress_true(
    force_corr, longitudination_corr, height, area)

### 3rd step ###
# get the transition from elast to plast and get the elast slope

elast_plast_trans = transition

slope_elast = getslopeelast.get_slope_elast(strain_true, stress_true, transition)

print('slope_elast: ' + str(slope_elast))
### 4th step ###
# calculate strain plast 
strain_plast = calcplaststrain.calc_plast_strain(
    strain_true, stress_true, slope_elast)
    
# corrected values

# correct everything refering to the constant stress level
zero_time = time_equal_corr[transition]
time_corr_final = time_equal_corr - zero_time

# most important step in the macro
# this one has to perform perfectly!
time_corr_filtered, strain_plast_filtered, window_errors, window_fitparas = filterdata.filter_data(strain_plast, time_corr_final, slope_window_size, nopts, strain_window_size)

if bool_cde == True:
    calcdeltaerror.calc_delta_error(window_fitparas, window_errors)

strainrate_plast_filtered = calcplaststrainrate.calc_plast_strainrate_with_fit(time_corr_filtered, strain_plast_filtered)
strainrate_plast_filtered_log = np.log10(strainrate_plast_filtered)

strain_plast_means_filtered = calcplaststrainrate.get_corresponding_means(
        strain_plast_filtered)
# add the last strain value and the estimated strainrate for this point
addlastvalue.add_last_value(
        strainrate_plast_filtered_log, strain_plast_means_filtered, strain_plast)

strainrate_plast_orig = calcplaststrainrate.calc_plast_strainrate_with_fit(
    time_corr, strain_plast)
    
strain_plast_means_orig = calcplaststrainrate.get_corresponding_means(
    strain_plast)

# strain in percent
strain_plast_means_orig = strain_plast_means_orig * 100
strain_plast_means_filtered = strain_plast_means_filtered * 100

strain_plast = strain_plast * 100
strain_plast_filtered = strain_plast_filtered * 100


print('number of points before filter: ' + str(strain_plast.size))
print('number of points after filter: ' + str(strain_plast_filtered.size))

# plotting

plot.plot_setup(save_path, time_corr_filtered, strain_plast_filtered, strain_plast_means_filtered, strainrate_plast_filtered, strain_plast, time_corr, strain_plast_means_orig, strainrate_plast_orig)

# write summary file
writefile.write_summary((strain_plast_means_orig, strainrate_plast_orig, strain_plast_filtered, strainrate_plast_filtered, time_corr, strain_true, stress_true))





