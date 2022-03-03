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


def stations_highest_rel_level(stations, N):
    def l(x): return x.relative_water_level()

    # proper_stations is the list of all stations which have a non "None" realtive water level
    proper_stations = [x for x in stations if not x.relative_water_level() is None]

    # sort proper_stations by relative_water_level
    proper_stations.sort(key=l, reverse = True)

    return proper_stations[:N]
