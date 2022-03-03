# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from cProfile import label
from turtle import color, distance
from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
import matplotlib.pyplot as plt

def stations_by_distance(stations, p):
    ''' returns distance from a co-ordinate from stations'''
    station_and_distances = []
    for station in stations:
        coordinate = station.coord
        distance = haversine(p, coordinate)
        station_and_distances.append((station, distance))
    station_and_distances.sort(key=sorting_distances)
    return station_and_distances  # for testing, remove after function implementation


def sorting_distances(station):
    distance = station[1]
    return distance


def stations_within_radius(stations, centre, r):
    ''' return a list of stations within radius r from centre '''

    # Order the stations and get a list with distances from centre
    stations_ordered = stations_by_distance(stations, centre)

    # Return a list of station names where their distance is < r
    near_stations = []
    for i in stations_ordered:
        if i[1] <= r:
            near_stations.append(i[0])
    return near_stations


def rivers_with_station(stations) -> set:
    """returns a set of rivers"""
    DuplicateRivers = []
    for station in stations:
        DuplicateRivers.append(station.river)
    Rivers = set(DuplicateRivers)
    return Rivers



def stations_by_river(stations) -> dict:
    """returns a dictionary of stations and rivers with rivers as the key"""
    riverDictionary = {}
    station_and_river = []
    for station in stations:
        station_and_river.append((station.name,station.river))
    station_and_river.sort(key=sorting_rivers)
    empty = []
    current = ""
    for data in station_and_river:
        if current == data[1]:
            empty.append(data[0])
        else:
            empty.sort()
            riverDictionary[current] = empty
            empty = [data[0]]
            current = data[1]
    empty.sort()
    riverDictionary[current] = empty
    return riverDictionary
        

def sorting_rivers(station):
    """sorting function for stations_by_rivers"""
    river = station[1]
    return river

def rivers_by_station_number(stations, N):
    ''' returns a list of N rivers with the greatest number of monitoring stations '''

    stations_by_river_dict = stations_by_river(stations)

    # A list of tuples in the form (river name, number of stations associated with that river)
    river_station_number = []

    # create river_station_number
    for i in stations_by_river_dict:
        river_station_number.append((i, len(stations_by_river_dict[i])))

    greatest = 0  # greatest number of stations

    # find greatest number of stations
    for i in river_station_number:
        if i[1] > greatest:
            greatest = i[1]

    rivers = []  # rivers to be returned

    while len(rivers) < N:

        # add all rivers with 'greatest' number of rivers to the list
        for i in river_station_number:
            if i[1] == greatest:
                rivers.append(i)
        greatest -= 1

    return rivers

#plots water levels for a station
def plot_water_levels(station, dates, levels, show=True):
    # Plot
    plt.plot(dates, levels, label='water data level')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    if station.typical_range_consistent():
        plt.axhline(y=station.typical_range[1], label="high", color = 'r',linestyle='-')
        plt.axhline(y=station.typical_range[0], label ="low", color = 'y',linestyle='-')
    plt.legend()

    if show:
        plt.show()

    return plt