from floodsystem.geo import plot_water_levels
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels


def sorts(station):
    if not station.latest_level:
        return 0.0
    if station.latest_level > 100:
        return 0.0
    return station.latest_level


def test_station_plotting():
    stations = build_station_list()
    update_water_levels(stations)
    stations.sort(key=sorts, reverse=True)
    count = 0
    for station in stations:
        dt = 10
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
        if dates:
            assert plot_water_levels(station, dates, levels) == None
            count = count + 1
        if count == 1:
            assert dates != None
            assert levels != None
            break