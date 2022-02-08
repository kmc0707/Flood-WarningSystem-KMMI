from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def test_inconsistent_typical_range_stations():
    """testing inconsistent_typical_range_stations function"""
    stations = build_station_list()
    inconsistants = inconsistent_typical_range_stations(stations)
    assert len(inconsistants) > 0
    for station in inconsistants:
        if station.typical_range:
            if ((station.typical_range[1] - station.typical_range[0]) > 0):
                assert False