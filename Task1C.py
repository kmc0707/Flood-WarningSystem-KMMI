from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    ''' Requirements for Task 1C'''

    stations = build_station_list()

    # Print stations with 10km of Cambridge city centre:
    stations_near_cam = stations_within_radius(stations, (52.2053, 0.1218), 10)
    station_names = [i.name for i in stations_near_cam]
    station_names.sort()
    print(station_names)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
