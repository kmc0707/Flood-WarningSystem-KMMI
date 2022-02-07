from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Requirements for Task 1D"""
    stations = build_station_list()
    rivers = list(rivers_with_station(stations))
    rivers.sort()
    print(len(rivers))
    print(rivers[:10])
    dic = stations_by_river(stations)
    print(dic["River Aire"])
    print(dic["River Cam"])
    print(dic["River Thames"])
    

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
