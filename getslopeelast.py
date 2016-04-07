import linfit

def get_slope_elast(strain_true, stress_true, trans_elast_plast_index):
    
    slope_elast = linfit.linfit(strain_true[:trans_elast_plast_index+1], stress_true[:trans_elast_plast_index+1])[0][0]

    return slope_elast
