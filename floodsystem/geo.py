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
    return [("test1", 5), ("test2", 15)] #for testing, remove after function implementation

def stations_within_radius(stations, centre, r):
    ''' return a list of stations within radius r from centre '''
    stations_ordered = stations_by_distance(stations, centre)
    return [i[0] if i[1] <= r else None for i in stations_ordered]
    