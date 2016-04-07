# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:54:02 2015

@author: Lukas Gartmair
"""
import gettransition

def get_force_transition(time, force):
    
    window_size = 2
    constant_force_level = gettransition.get_transition(time, force, window_size)
    return constant_force_level
