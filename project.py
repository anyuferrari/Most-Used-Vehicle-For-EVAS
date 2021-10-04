import csv
from datetime import datetime, timedelta
# This project will be looking into the data provided by NASA about EVA's (extra vehicular activities) performed
# by US and Russian Astronauts from 1965 up to date.
# The purpose will be to analyze which was the most used vehicle for this activity, taking in account fro how many hours 
# they were used 

vehicles = {}
time_zero = datetime.strptime('00:00', '%H:%M')
with open("Extra-vehicular_Activity__EVA__-_US_and_Russia.csv", newline = "") as evas:
    evas_list = csv.DictReader(evas)
    for item in evas_list:
        try:
            if item["Vehicle"] not in vehicles:
                dur = (datetime.strptime(item["Duration"], "%H:%M") - time_zero)
                vehicles[item["Vehicle"]] = dur
            else:
                vehicles[item["Vehicle"]] += (datetime.strptime(item["Duration"], "%H:%M") - time_zero)
        except:
            pass

max_time = timedelta(hours = 0)
most_used = ""
for vehicle, time in vehicles.items():
    if time > max_time:
        most_used = vehicle
        max_time = time
most_used_list = most_used.split()
most_used_clean =[]
most_used_final = " ".join(most_used_list)
print("Astronauts on the {} vehicle were the ones with the most EVA (Extra-Vehicular Activity) time, with {}".format(most_used_final,max_time))