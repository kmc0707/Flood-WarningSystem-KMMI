"""
This module contains functions relating to the analysis of flood data
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
from floodsystem.datafetcher import fetch_measure_levels


def polyfit(dates, levels, p):
    """fits a polynomial of order 'p' to the data of dates and levels"""
    dates = matplotlib.dates.date2num(dates)
    d0 = dates[0]  # offset (first time value)

    dates = [i - d0 for i in dates]

    # Find coefficients of best-fit polynomial f(x)
    p_coeff = np.polyfit(dates, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)
    
    return poly, d0
