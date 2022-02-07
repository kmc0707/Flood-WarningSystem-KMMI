from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    stations_and_distance = stations_by_distance(stations, (52.2053, 0.1218))
    firstTen = stations_and_distance[:10]
    lastTen = stations_and_distance[-10:]
    firstTenCorrected = []
    lastTenCorrected = []
    for data in firstTen:
        firstTenCorrected.append((data[0].name, data[0].town, data[1]))
    print(firstTenCorrected)
    for data in lastTen:
        lastTenCorrected.append((data[0].name, data[0].town, data[1]))
    print(lastTenCorrected)



if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
