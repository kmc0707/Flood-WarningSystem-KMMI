from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

def test_dictionary():
    """Testing stations_by_river to make sure it returns a dictionary with length"""
    stations = build_station_list()
    dic = stations_by_river(stations)
    assert len(dic.keys()) > 0