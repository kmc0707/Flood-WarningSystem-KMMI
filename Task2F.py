from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def run():
    stations = build_station_list()
    update_water_levels(stations)

    flooded_stations = stations_highest_rel_level(stations, 2)
    dates, levels = fetch_measure_levels(flooded_stations[1].measure_id, dt=datetime.timedelta(days=2))
    poly = polyfit(dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
