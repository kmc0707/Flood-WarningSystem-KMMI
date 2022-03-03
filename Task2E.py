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


def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations.sort(key=sorts, reverse=True)
    count = 0
    for station in stations:
        dt = 10
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
        if dates:
            plot_water_levels(station, dates, levels)
            count = count + 1
        if count == 5:
            break

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
