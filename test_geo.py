''' Unit test for geo.py '''

from floodsystem.geo import stations_within_radius, rivers_by_station_number
from floodsystem.stationdata import build_station_list


# Task 1C

def test_stations_within_radius():
    stations = stations_within_radius(build_station_list(), (52.2053, 0.1218), 10)
    assert len(stations) > 0
    assert isinstance(stations, list)


# Task 1E

def test_rivers_by_station_number():
    rivers = rivers_by_station_number(build_station_list(), 10)
    assert len(rivers) >= 10
    assert isinstance(rivers, list)
    assert len(rivers[0]) == 2
    assert isinstance(rivers[0], tuple)