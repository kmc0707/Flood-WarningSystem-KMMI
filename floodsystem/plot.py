"""
Module contains functions for plotting relevant graphs
"""

from floodsystem.analysis import polyfit
from floodsystem.geo import plot_water_levels
import numpy as np
import matplotlib.dates

def plot_water_level_with_fit(station, dates, levels, p):
    """plots water levels with a polynomial fit"""
    plt = plot_water_levels(station, dates, levels, show=False)

    poly, d0 = polyfit(dates, levels, p)

    poly_levels = []

    for i in dates:
        poly_levels.append(poly(matplotlib.dates.date2num(i) - d0))

    plt.plot(dates, poly_levels, label="polynomial approximation")

    # Display plot
    plt.legend()
    plt.show()

