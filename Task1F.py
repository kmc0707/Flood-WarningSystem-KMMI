from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""
    stations = build_station_list()
    inconsistants = inconsistent_typical_range_stations(stations)
    names = []
    for data in inconsistants:
        names.append(data.name)
    names.sort()
    print(names)
    

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
