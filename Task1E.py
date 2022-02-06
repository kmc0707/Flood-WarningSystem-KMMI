from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    ''' Requirements for Task 1E'''
    
    stations = build_station_list()

    # Print 9 or more rivers the greatest number of stations:
    print(rivers_by_station_number(stations, 9))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
