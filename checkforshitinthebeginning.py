# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:17:48 2015

@author: Lukas
"""

def check_for_equals_in_the_beginning(longitudination_orig):
    # n is the number of n-first data points for the search
    n = 30
    nonequal = 0
    for (x, s) in enumerate(longitudination_orig):
        if x < n and x < longitudination_orig.size :
            if s != longitudination_orig[x+1]:
                if x == 0:
                    nonequal = 0
                elif x > 0:
                    nonequal = x-1
                break

    return nonequal
