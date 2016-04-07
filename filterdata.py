import linfit
import numpy as np
import subwindows
import getdistancetotrendindices
import getclosestpoints
import windowfunctions

def get_trend_pivot(X, Y):
    
    fit = linfit.linfit(X,Y)

    m_pivot = fit[0][0]
    t_pivot = fit[0][1]
    
# 2nd bunch = return_of_linfit[-1]
# 3rd [da,db] = bunch.fiterr
    
    bunch = fit[-1]
    fiterr = bunch.fiterr
    dm_pivot = fiterr[0]
    dt_pivot = fiterr[1]

    return m_pivot, t_pivot, dm_pivot, dt_pivot

def get_ratios_of_slopes(time_corr,strain_plast, slope_window_size):

    windows_t, windows_st = subwindows.sub_windows(time_corr, strain_plast, slope_window_size)
    m_subs = []
    for i,w in enumerate(windows_t):
        m_sub = get_trend_pivot(w, windows_st[i])[0]
        m_subs.append(m_sub)
    slope_ratios = []
    for i,m in enumerate(m_subs):
        if i > 0:
            ratio = (m / m_subs[i - 1])
            slope_ratios.append(ratio)
    return np.asarray(slope_ratios)
    
def filter_data(strain_plast, time_corr, window_size, nopts, strain_window_size):
    
    slope_ratios = get_ratios_of_slopes(time_corr, strain_plast, window_size)
    print('slope_ratios: ' + str(slope_ratios))    
    
    time_corr_splitted, strain_plast_splitted = windowfunctions.split_windows(slope_ratios, time_corr, strain_plast, strain_window_size)
    
    time_filtered = np.arange(0)
    strain_plast_filtered = np.arange(0)
    window_fitparas = []
    window_errors = []

    for index,t in enumerate(time_corr_splitted):
        if t.size < 3:
            # for example the last window could raise an error if only two values left
            print('shit')            
            pass
        else:
            trend = get_trend_pivot(t, strain_plast_splitted[index])
            m_sub = trend[0]
            t_sub = trend[1]
            dm_sub = trend[2]
            dt_sub = trend[3]
            
            window_fitparas.append([m_sub, t_sub])
            window_errors.append([dm_sub, dt_sub])
        #    
            # get the distances from the mean and the corresponding index sort
            ranked_indices = getdistancetotrendindices.get_distance_to_trend_indices(
            m_sub, t_sub, strain_plast_splitted[index])
            
            # finally filter 
            sub_time_filtered, sub_strain_filtered = getclosestpoints.get_clostest_points_to_trend(nopts, ranked_indices, t, strain_plast_splitted[index])
            time_filtered = np.concatenate((time_filtered, sub_time_filtered))
            strain_plast_filtered = np.concatenate((strain_plast_filtered,sub_strain_filtered))

    return time_filtered, strain_plast_filtered, window_errors, window_fitparas
