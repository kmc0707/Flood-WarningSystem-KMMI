''' Unit test for geo.py '''

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

# Task 1C


def test_stations_within_radius():
    stations = stations_within_radius(build_station_list(), (52.2053, 0.1218), 10)
    print(type(stations))
    assert len(stations) > 0
