from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station

def test_no_duplicates():
    """testing rivers_with_station"""
    stations = build_station_list()
    rivers = list(rivers_with_station(stations))
    rivers.sort()
    assert len(rivers) > 0
    assert len(rivers) == len(set(rivers))
