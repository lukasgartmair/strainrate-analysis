import slopedetection
import movingaverage
import peakdetection
import numpy as np
import matplotlib.pyplot as pl

def find_saturation_point_v2(X,Y):
    
#    http://www.graphpad.com/guides/prism/6/curve-fitting/index.htm?reg_one_site_specific.htm

    kd = ((np.amax(Y)*X)/Y)-X
    
    saturation_index = np.argmax(kd)
    return saturation_index

def find_saturation_point_v1(arrx,arry):
    slope_changes = get_slope_changes(arrx,arry)
    abs_slope_changes = np.absolute(slope_changes)
    median = np.median(abs_slope_changes)
    saturation_array = np.where(abs_slope_changes <= median)[0]
                    
    for i,s in enumerate(saturation_array):
        if np.logical_and((s+1 in saturation_array),(s+2 in saturation_array)):
            saturation_index = saturation_array[i]
            break
    
    return saturation_index

def get_slope_changes(X,Y):
    window_fraction = 5
    slope_changes = []
    slope_changes = slopedetection.slopedec(X, Y, window_fraction)
    return slope_changes

def get_index_of_trans(slopes_avg):
    peak_crit = 5
    quantil = 0.1
    abs_slopes_avg = np.absolute(slopes_avg)     
    first_quantil = abs_slopes_avg[0:(round(abs_slopes_avg.size * quantil))]
    transitions_maxima = peakdetection.peakdet(first_quantil, peak_crit)[0]
    transitions_minima = peakdetection.peakdet(first_quantil, peak_crit)[1]
    
    if transitions_minima.size and transitions_maxima.size != 0:
        transitions = np.concatenate((transitions_maxima,transitions_minima), axis=0)
    elif transitions_maxima.size != 0:
        transitions = transitions_maxima
    elif transitions_minima.size != 0:
        transitions = transitions_minima
    else:
        # hier muss noch eine bedingung rein
        # was paasiert wenn beide null sind
        print('no peaks detected')
    trans_index_tmp = np.where(transitions[:,1] == np.amax(transitions[:,1]))[0]
    # plus 2 wegen überlappung bei slopedetection
    trans_index = trans_index_tmp[0] + 2
    
    return trans_index

def get_transition(X, Y, window_size):

    slope_changes = get_slope_changes(X, Y)
    window_size = 5
    slopes_avg = movingaverage.movingaverage(slope_changes, window_size)
    
#    pl.plot(np.absolute(slopes_avg))
#    pl.legend()
    trans = get_index_of_trans(slopes_avg)  
    return trans

# unit test

import unittest

# set up the test cases
test_window_size = 5
X_unittest = np.arange(30)
Y_unittest_all_zero = np.zeros(30)
Y_unittest_middlepeak = np.copy(Y_unittest_all_zero)
Y_unittest_middlepeak[5] = 100
Y_unittest_random1 = np.array([ 19,  79,  78,  29,  41,  41,  35,  60,  11,  54, 100, 100,  42,
        42,  24,  27,  19,  29,  76,  98,  47,  81,  12,  68,  12,  11,
        23,  94,  16,  86])
        
Y_unittest_random2 = np.array([15, 61,  5, 62, 45, 24, 32, 84, 19, 37, 32, 85, 63, 54, 26, 57, 21,
       40, 80,  2, 47, 99, 70, 38,  3, 22, 34, 61, 66, 28])

X_sat = np.array([  9.00000000e-02,   2.90000000e-01,   4.90000000e-01,
         6.90000000e-01,   8.90000000e-01,   1.09000000e+00,
         1.29000000e+00,   1.49000000e+00,   1.69000000e+00,
         1.89000000e+00,   2.09000000e+00,   2.29000000e+00,
         2.49000000e+00,   2.69000000e+00,   2.89000000e+00,
         3.09000000e+00,   3.29000000e+00,   3.49000000e+00,
         3.69000000e+00,   3.89000000e+00,   4.09000000e+00,
         4.29000000e+00,   4.49000000e+00,   4.69000000e+00,
         4.89000000e+00,   5.09000000e+00,   5.69000000e+00,
         6.69000000e+00,   7.69000000e+00,   8.69000000e+00,
         9.69000000e+00,   1.06900000e+01,   1.36900000e+01,
         2.11900000e+01,   3.11900000e+01,   5.11900000e+01,
         8.11900000e+01,   1.11190000e+02,   1.56190000e+02,
         2.46190000e+02,   3.66190000e+02,   4.88450000e+02,
         6.10330000e+02,   9.70250000e+02,   1.57025000e+03,
         2.17025000e+03,   2.77025000e+03,   3.37025000e+03,
         3.97025000e+03,   4.57025000e+03,   5.17025000e+03,
         5.77025000e+03,   6.37025000e+03,   6.97025000e+03,
         7.57025000e+03,   8.17025000e+03,   8.77025000e+03,
         9.37025000e+03,   9.97025000e+03,   1.05702500e+04,
         1.11702500e+04,   1.17702500e+04,   1.23702500e+04,
         1.29702500e+04,   1.35702500e+04,   1.41702500e+04,
         1.47702500e+04,   1.53702500e+04,   1.59702500e+04,
         1.65702500e+04,   1.71702500e+04,   1.77702500e+04,
         1.83702500e+04,   1.89702500e+04,   1.95702500e+04,
         2.01702500e+04,   2.07702500e+04,   2.13702500e+04,
         2.19702500e+04,   2.25702500e+04,   2.31702500e+04,
         2.37702500e+04,   2.43702500e+04,   2.49702500e+04,
         2.55702500e+04,   2.61702500e+04,   2.67702500e+04,
         2.73702500e+04,   2.79702500e+04,   2.85702500e+04,
         2.91702500e+04,   2.97702500e+04,   3.03702500e+04,
         3.09702500e+04,   3.15702500e+04,   3.21702500e+04,
         3.27702500e+04,   3.33702500e+04,   3.39702500e+04,
         3.45702500e+04,   3.51702500e+04,   3.57702500e+04,
         3.63702500e+04,   3.69702500e+04,   3.75702500e+04,
         3.81702500e+04,   3.87702500e+04,   3.93702500e+04,
         3.99702500e+04,   4.05702500e+04,   4.11702500e+04,
         4.17702500e+04,   4.23702500e+04,   4.29702500e+04,
         4.35702500e+04,   4.41702500e+04,   4.47702500e+04,
         4.53702500e+04,   4.59702500e+04,   4.65702500e+04,
         4.71702500e+04,   4.77702500e+04,   4.83702500e+04,
         4.89702500e+04,   4.95702500e+04,   5.01702500e+04,
         5.07702500e+04,   5.13702500e+04,   5.19702500e+04,
         5.25702500e+04,   5.31702500e+04,   5.37702500e+04,
         5.43702500e+04,   5.49702500e+04,   5.55702500e+04,
         5.61702500e+04,   5.67702500e+04,   5.73702500e+04,
         5.79702500e+04,   5.85702500e+04,   5.91702500e+04,
         5.97702500e+04,   6.02373500e+04,   6.20087800e+04,
         6.52087900e+04,   6.84087900e+04,   7.16087900e+04,
         7.48087900e+04,   7.80087900e+04,   8.12087900e+04,
         8.44087900e+04,   8.76087900e+04,   9.08087900e+04,
         9.40087900e+04,   9.72087900e+04,   1.00408790e+05,
         1.03608790e+05,   1.06808790e+05,   1.10008790e+05,
         1.13208790e+05,   1.16408790e+05,   1.19608790e+05,
         1.22808790e+05,   1.26008790e+05,   1.29208790e+05,
         1.32408790e+05,   1.35608790e+05,   1.38808790e+05,
         1.42008790e+05,   1.44808790e+05,   1.47208790e+05,
         1.49608790e+05,   1.52008790e+05,   1.54408790e+05,
         1.56808790e+05,   1.59208790e+05,   1.61608790e+05,
         1.64008790e+05,   1.66408790e+05,   1.68808790e+05,
         1.71208790e+05,   1.73608790e+05,   1.76008790e+05,
         1.78408790e+05,   1.80808790e+05,   1.83208790e+05,
         1.85608790e+05,   1.88008790e+05,   1.90408790e+05,
         1.92808790e+05,   1.95208790e+05,   1.97608790e+05,
         2.00008790e+05,   2.02408790e+05,   2.04808790e+05,
         2.07208790e+05,   2.09608790e+05,   2.12008790e+05,
         2.14408790e+05,   2.16808790e+05,   2.19208790e+05,
         2.21608790e+05,   2.24008790e+05,   2.26408790e+05,
         2.28808790e+05,   2.31208790e+05,   2.33608790e+05,
         2.36008790e+05,   2.38408790e+05,   2.40808790e+05,
         2.43208790e+05,   2.45608790e+05,   2.48008790e+05,
         2.50408790e+05,   2.52808790e+05,   2.55208790e+05,
         2.57608790e+05,   2.60008790e+05,   2.62408790e+05,
         2.64808790e+05,   2.67508790e+05,   2.70508790e+05,
         2.73508790e+05,   2.76508800e+05,   2.79508800e+05,
         2.82508800e+05,   2.85508800e+05,   2.88508800e+05,
         2.91508800e+05,   2.94508800e+05,   2.97508800e+05,
         3.00508800e+05,   3.03508800e+05,   3.06508800e+05,
         3.09508800e+05,   3.12508800e+05,   3.15508800e+05,
         3.18508800e+05,   3.21508800e+05,   3.24508800e+05,
         3.27508800e+05,   3.30508800e+05,   3.33508800e+05,
         3.36508800e+05,   3.39508800e+05,   3.42508800e+05,
         3.45508800e+05,   3.48508800e+05,   3.51508800e+05,
         3.54508800e+05,   3.57508800e+05,   3.60508800e+05,
         3.63508800e+05,   3.66508800e+05,   3.69508800e+05,
         3.72508800e+05,   3.75508800e+05,   3.78508800e+05,
         3.81508800e+05,   3.84508800e+05,   3.87508800e+05,
         3.90508800e+05,   3.93508800e+05,   3.96508800e+05,
         3.99508800e+05,   4.02508800e+05,   4.05508800e+05,
         4.08508800e+05,   4.11508800e+05,   4.14708800e+05,
         4.18108800e+05,   4.21508800e+05,   4.24908800e+05,
         4.28308800e+05,   4.31708800e+05,   4.35108800e+05,
         4.38508800e+05,   4.41908800e+05,   4.45308800e+05,
         4.48708800e+05,   4.52108800e+05,   4.55508800e+05,
         4.58908800e+05,   4.62308800e+05,   4.65708800e+05,
         4.69108800e+05,   4.72508800e+05,   4.75908800e+05,
         4.79308800e+05,   4.82708800e+05,   4.86108810e+05,
         4.89508810e+05,   4.92908810e+05,   4.96308810e+05,
         4.99708810e+05,   5.03108810e+05,   5.06508810e+05,
         5.09908810e+05,   5.13308810e+05,   5.16708810e+05,
         5.20108810e+05,   5.23508810e+05,   5.26908810e+05,
         5.30308810e+05,   5.33708810e+05,   5.37108810e+05,
         5.40508810e+05,   5.43908810e+05,   5.47308810e+05,
         5.50708810e+05,   5.54108810e+05,   5.57508810e+05,
         5.60908810e+05,   5.64308810e+05,   5.67708810e+05,
         5.71108810e+05,   5.74508810e+05,   5.77908810e+05,
         5.81308810e+05,   5.84708810e+05,   5.88108810e+05,
         5.91508810e+05,   5.94908810e+05,   5.98308810e+05,
         6.01708810e+05,   6.05108810e+05,   6.08508810e+05,
         6.11908810e+05,   6.15308810e+05,   6.18708810e+05,
         6.22108810e+05,   6.25508810e+05,   6.28908810e+05,
         6.32308810e+05,   6.35708810e+05,   6.39108810e+05,
         6.42508810e+05,   6.45908810e+05,   6.49308810e+05,
         6.52708810e+05,   6.56108810e+05,   6.59508810e+05,
         6.62908810e+05,   6.66308810e+05,   6.69708810e+05,
         6.73108810e+05,   6.76508810e+05,   6.79908810e+05,
         6.83308810e+05,   6.86708810e+05,   6.90108810e+05,
         6.93508810e+05,   6.96908820e+05,   7.00308820e+05,
         7.03708820e+05,   7.07108820e+05,   7.10508820e+05,
         7.13908820e+05,   7.17308820e+05,   7.20708820e+05,
         7.24108820e+05,   7.27508820e+05,   7.30908820e+05,
         7.34308820e+05,   7.37708820e+05,   7.41108820e+05,
         7.44508820e+05])
       
Y_sat = np.array([ -1.16052247e-04,  -3.53661072e-04,  -1.71735632e-04,
        -2.30286348e-04,  -3.09748035e-04,  -1.48733565e-04,
        -3.72120688e-04,   4.98767531e-05,  -5.03140605e-05,
         1.49716592e-04,   1.33724926e-04,   5.53171375e-04,
         5.52652394e-04,   6.26165901e-04,   4.97910588e-04,
         1.35486943e-04,   5.67082388e-05,  -2.88388100e-04,
        -2.47375808e-04,  -5.93670275e-04,  -2.78222627e-04,
        -5.30404398e-04,  -3.20727527e-04,  -6.05625903e-04,
        -3.42882224e-04,  -5.56179333e-04,  -3.76990173e-04,
        -3.30814813e-04,  -2.83714414e-04,  -1.98409198e-04,
        -2.40191679e-04,  -1.76675517e-04,  -1.33520743e-04,
        -4.12973440e-05,   1.44803046e-05,   1.18805161e-04,
         2.99534034e-04,   3.74849411e-04,   4.65232186e-04,
         5.78860733e-04,   6.54631173e-04,   7.21504754e-04,
         8.29266498e-04,   9.30969649e-04,   1.27482693e-03,
         1.18703591e-03,   1.26290847e-03,   1.29173262e-03,
         1.34042978e-03,   1.41457120e-03,   1.46787734e-03,
         1.51217712e-03,   1.53431287e-03,   1.58954293e-03,
         1.62008988e-03,   1.63834288e-03,   1.70046498e-03,
         1.73969968e-03,   1.76736227e-03,   1.79592355e-03,
         1.80355971e-03,   1.82869523e-03,   1.82789889e-03,
         1.88226548e-03,   1.90277051e-03,   1.92438852e-03,
         1.95485205e-03,   1.99565090e-03,   2.00062363e-03,
         2.01799847e-03,   2.03547172e-03,   2.07853044e-03,
         2.08922961e-03,   2.10073865e-03,   2.11571593e-03,
         2.14661031e-03,   2.16109503e-03,   2.19957828e-03,
         2.19456436e-03,   2.19537004e-03,   2.22195391e-03,
         2.22277940e-03,   2.23459587e-03,   2.24295539e-03,
         2.27523214e-03,   2.26601963e-03,   2.29188580e-03,
         2.32079014e-03,   2.36841595e-03,   2.38421759e-03,
         2.40959139e-03,   2.40236889e-03,   2.44473349e-03,
         2.46563465e-03,   2.45411736e-03,   2.45869872e-03,
         2.47156536e-03,   2.48309842e-03,   2.49490369e-03,
         2.52842548e-03,   2.51402233e-03,   2.52160456e-03,
         2.54092304e-03,   2.55732145e-03,   2.58033687e-03,
         2.56515206e-03,   2.60673644e-03,   2.61104547e-03,
         2.62200923e-03,   2.64511215e-03,   2.66716395e-03,
         2.66829736e-03,   2.70756876e-03,   2.69836961e-03,
         2.69497893e-03,   2.72139106e-03,   2.72781881e-03,
         2.75801650e-03,   2.78161660e-03,   2.80929406e-03,
         2.84195023e-03,   2.83601233e-03,   2.84486578e-03,
         2.85574879e-03,   2.87667120e-03,   2.85886623e-03,
         2.90961962e-03,   2.92278347e-03,   2.95816259e-03,
         2.95206537e-03,   2.94254138e-03,   2.93395193e-03,
         2.93011794e-03,   2.96538438e-03,   2.97767984e-03,
         3.00220207e-03,   2.99921647e-03,   3.01995519e-03,
         3.04566790e-03,   3.07169247e-03,   3.08722611e-03,
         3.10204311e-03,   3.09215778e-03,   3.11321646e-03,
         3.23791399e-03,   3.20197162e-03,   3.29145218e-03,
         3.38130375e-03,   3.44252069e-03,   3.55744414e-03,
         3.63192367e-03,   3.76623047e-03,   3.80431783e-03,
         3.90942143e-03,   3.92532614e-03,   4.02743223e-03,
         4.09628480e-03,   4.20478095e-03,   4.23356244e-03,
         4.32512090e-03,   4.42034108e-03,   4.52077189e-03,
         4.60551510e-03,   4.75277530e-03,   4.91156477e-03,
         5.03369027e-03,   5.11735615e-03,   5.24418888e-03,
         5.41999197e-03,   5.41101680e-03,   5.57547447e-03,
         5.59852925e-03,   5.68653492e-03,   5.76860785e-03,
         5.83319558e-03,   5.93487350e-03,   6.01993814e-03,
         6.08523178e-03,   6.13509250e-03,   6.18153156e-03,
         6.44651100e-03,   6.47267829e-03,   6.70903336e-03,
         6.52559168e-03,   6.59099058e-03,   6.67246872e-03,
         6.83168779e-03,   6.80919799e-03,   6.88893271e-03,
         6.94933345e-03,   7.02082144e-03,   7.09084912e-03,
         7.16944640e-03,   7.28005895e-03,   7.33681747e-03,
         7.39555630e-03,   7.45255279e-03,   7.53029346e-03,
         7.60969891e-03,   7.65079876e-03,   7.72728641e-03,
         7.76830743e-03,   7.80115565e-03,   7.87173702e-03,
         8.02013966e-03,   8.05486400e-03,   8.03066577e-03,
         8.01430913e-03,   8.04787722e-03,   8.17166541e-03,
         8.17620866e-03,   8.27229085e-03,   8.29257426e-03,
         8.30440059e-03,   8.43466710e-03,   8.45493679e-03,
         8.43294934e-03,   8.52579060e-03,   8.47425167e-03,
         8.50237812e-03,   8.51329511e-03,   8.57194045e-03,
         8.64025465e-03,   8.68430337e-03,   8.70967062e-03,
         8.73989605e-03,   8.76821814e-03,   8.80424102e-03,
         8.85425762e-03,   8.93754038e-03,   8.98053620e-03,
         9.03305094e-03,   9.07733863e-03,   9.13702059e-03,
         9.18192464e-03,   9.22842407e-03,   9.24903306e-03,
         9.28659015e-03,   9.25708102e-03,   9.29838492e-03,
         9.31113762e-03,   9.34326580e-03,   9.37724872e-03,
         9.42940399e-03,   9.44221074e-03,   9.44958828e-03,
         9.48702707e-03,   9.53043397e-03,   9.55616331e-03,
         9.58246252e-03,   9.58569855e-03,   9.60574385e-03,
         9.63370165e-03,   9.65944142e-03,   9.66613031e-03,
         9.68807751e-03,   9.74834604e-03,   9.73091950e-03,
         9.75617935e-03,   9.77882196e-03,   9.81158429e-03,
         9.82267979e-03,   9.85473590e-03,   9.87747328e-03,
         9.90864663e-03,   9.90912347e-03,   9.94078948e-03,
         9.96274177e-03,   9.97785507e-03,   9.95997700e-03,
         9.94708283e-03,   9.96401631e-03,   9.93751958e-03,
         9.95996775e-03,   9.99489977e-03,   1.00219225e-02,
         1.00473593e-02,   1.00789069e-02,   1.01277305e-02,
         1.01122836e-02,   1.01383075e-02,   1.01793380e-02,
         1.02007574e-02,   1.01861730e-02,   1.02225563e-02,
         1.02438920e-02,   1.02542216e-02,   1.02789909e-02,
         1.02906823e-02,   1.03363790e-02,   1.03468555e-02,
         1.03646188e-02,   1.03977829e-02,   1.03721096e-02,
         1.03419044e-02,   1.05114062e-02,   1.05444628e-02,
         1.03629277e-02,   1.04260210e-02,   1.03937864e-02,
         1.04992700e-02,   1.05907107e-02,   1.04887494e-02,
         1.04970648e-02,   1.04863541e-02,   1.05053294e-02,
         1.05686293e-02,   1.05614517e-02,   1.05729183e-02,
         1.06210014e-02,   1.06257573e-02,   1.06289975e-02,
         1.06487920e-02,   1.06763457e-02,   1.06757498e-02,
         1.06881049e-02,   1.07042802e-02,   1.07090583e-02,
         1.08973829e-02,   1.08725054e-02,   1.07415014e-02,
         1.07593351e-02,   1.07730658e-02,   1.07861263e-02,
         1.07866229e-02,   1.08110987e-02,   1.08909220e-02,
         1.08259684e-02,   1.08728584e-02,   1.09086359e-02,
         1.09445173e-02,   1.09302292e-02,   1.09245100e-02,
         1.09675334e-02,   1.09686352e-02,   1.09665625e-02,
         1.09928534e-02,   1.10350632e-02,   1.10270622e-02,
         1.10261156e-02,   1.10300389e-02,   1.11340266e-02,
         1.10765724e-02,   1.10703804e-02,   1.10927332e-02,
         1.10716723e-02,   1.10945832e-02,   1.10812707e-02,
         1.11084728e-02,   1.10838100e-02,   1.11083542e-02,
         1.11426389e-02,   1.10930151e-02,   1.11021746e-02,
         1.11311611e-02,   1.12038123e-02,   1.12029311e-02,
         1.12080179e-02,   1.12785742e-02,   1.13342343e-02,
         1.13489035e-02,   1.13661896e-02,   1.13766906e-02,
         1.14081717e-02,   1.14235888e-02,   1.14063128e-02,
         1.14214081e-02])

test_result_all_zero = 0
test_result_middlepeak = 2
test_result_random1 = 5
test_result_random2 = 6
test_result_sat = 52

class GetTransitionTest(unittest.TestCase):

    def test_get_transition(self):
        np.testing.assert_array_equal(get_transition(X_unittest,Y_unittest_middlepeak, test_window_size),test_result_middlepeak )
        np.testing.assert_array_equal(get_transition(X_unittest,Y_unittest_random1, test_window_size),test_result_random1 )
        np.testing.assert_array_equal(get_transition(X_unittest,Y_unittest_random2, test_window_size),test_result_random2 )
        
    def test_find_saturation_point(self):
        np.testing.assert_array_equal(find_saturation_point(X_sat,Y_sat),test_result_sat)
        
def main():
    unittest.main()
if __name__ == '__main__':
    main()
