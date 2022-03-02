"""
This module contains functions related to flood detection
"""


def stations_level_over_threshold(stations, tol):
    "returns stations where water level is greater than tol as a list of tuples "

    flooded_stations = []

    for i in stations:
        if i.relative_water_level() and i.relative_water_level() > tol:
            flooded_stations.append([i, i.relative_water_level()])

    return flooded_stations
