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
    ''' returns stations organised by river in the form {river: ["station", "station"]}'''
    pass  # TODO Kyle


def rivers_by_station_number(stations, N):
    ''' returns a list of N rivers with the greatest number of monitoring stations '''


    #stations_by_river_dict = stations_by_river(stations)

    stations_by_river_dict = {
        "river a" : ["station", "station"],
        "river b" : ["station", "station", "station", "station"],
        "river c" : ["station", "station", "station"],
        "river d" : ["station", "station", "station", "station"],
        "river e" : ["station", "station", "station"],
        "river f" : ["station", "station"],
    }    # for testing while stations_by_river_dict not implemented

    river_station_number = [] # A list of tuples in the form (river name, number of stations associated with that river)

    # create river_station_number
    for i in stations_by_river_dict:
        river_station_number.append((i, len(stations_by_river_dict[i])))

    greatest = 0 # greatest number of stations

    # find greatest number of stations
    for i in river_station_number:
        if i[1] > greatest:
            greatest = i[1]
    
    rivers = [] # rivers to be returned

    while len(rivers) < N:

        # add all rivers with 'greatest' number of rivers to the list
        for i in river_station_number:
            if i[1] == greatest:
                rivers.append(i[0])
        greatest -= 1

    return rivers
