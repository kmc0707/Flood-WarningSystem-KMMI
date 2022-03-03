import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

def run():
    severities = {}
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        severity = 0
        dt = 10
        if station.relative_water_level():
            severity = station.relative_water_level() * 10 #checks the current water levels so if already flooding then already gonna be severe
        try:
            dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        except:
            levels = None
        days = 1
        if levels:
            if levels[9] > levels[8]:
                for i in range (7):
                    if levels[8-i] > levels[8-i-1]:
                        days = days+1
                if days > 2 and days < 4:
                    severity = severity + 1
                if days >= 4 and days < 7:
                    severity = severity + 2
                if days >= 7:
                    severity = severity + 3
            
            if levels[9] < levels[8]:
                for i in range (7):
                    if levels[8-i] < levels[8-i-1]:
                        days = days+1
                if days > 2 and days < 4:
                    severity = severity - 1
                if days >= 4 and days < 7:
                    severity = severity - 2
                if days >= 7:
                    severity = severity - 3

            if station.latest_level:
                if station.latest_level > levels [9]:
                    severity = severity + 1
                if station.latest_level < levels [9]:
                    severity = severity - 1
        
        if severity >= 10:
            severities[station] = "Severe"
        elif severity < 10 and severity >= 7:
            severities[station] = "High"
        elif severity < 7 and severity >= 4:
            severities[station] = "Moderate"
        else:
             severities[station] = "Low"

        print("Flood risk for ", station.name, " is ", severities[station])



        


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()