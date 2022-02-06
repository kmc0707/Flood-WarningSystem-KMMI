# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    ''' docstring '''
    # Kyle todo
    return [("test1", 5), ("test2", 15)]  # for testing, remove after function implementation


def stations_within_radius(stations, centre, r):
    ''' return a list of stations within radius r from centre '''

    # Order the stations and get a list with distances from centre
    stations_ordered = stations_by_distance(stations, centre)

    # Return a list of station names where their distance is < r
    return [i[0] if i[1] <= r else None for i in stations_ordered]


def rivers_with_station(stations) -> set:
    ''' returns a list of rivers which have at least one monitoring station '''
    pass  # TODO Kyle


def stations_by_river(stations) -> dict:
    ''' returns stations organised by river in the form {river: "station"}'''
    pass  # TODO Kyle


def rivers_by_station_number(stations, N):
    ''' returns a list of N rivers with the greatest number of monitoring stations '''

    greatest = 0  # greatest number of rivers

    stations_by_river_dict = stations_by_river(stations)

    for i in stations_by_river_dict:
        pass
