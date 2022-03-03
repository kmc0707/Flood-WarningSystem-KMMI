from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
#from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def run():
    stations = build_station_list()
    update_water_levels(stations)

    flooded_stations = stations_highest_rel_level(stations, 6)
    for i in flooded_stations[1:]: #Ignore first station as it is an 'error' station (the data is bad :( )
        dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=2))
        #poly = polyfit(dates, levels, 4)

        plot_water_level_with_fit(i, dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
