from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def test_stations_distance():
    """Test stations_by distance returns something"""

    # Build list of stations
    stations = build_station_list()
    stations_and_distance = stations_by_distance(stations, (52.2053, 0.1218))
    assert len(stations_and_distance) > 0
    assert stations_and_distance[0][1] < stations_and_distance[len(stations_and_distance) - 1][1]

