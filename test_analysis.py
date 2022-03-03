'''unit test for analysis.py'''

from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import datetime

def test_polyfit():    
    stations = build_station_list()
    update_water_levels(stations)

    flooded_stations = stations_highest_rel_level(stations, 6)
    dates, levels = fetch_measure_levels(flooded_stations[2].measure_id, dt=datetime.timedelta(days=2))
    poly = polyfit(dates, levels, 4)

    assert isinstance(poly[1], float)
    assert isinstance(poly[0], np.poly1d)
