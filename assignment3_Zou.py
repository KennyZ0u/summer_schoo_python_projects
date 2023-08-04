import pandas
borough_dict = {'Brooklyn':0, 'Queens':0, 'Manhattan':0, 'Staten Island':0, 'Bronx':0, 'No Shooting Permit':0}
film_permits = pandas.read_csv("film_permits.csv")
events_column = film_permits["EventType"]
borough_column = film_permits["Borough"]
each_event = 0
for each_borough in borough_column:
    if events_column[each_event] == "Shooting Permit":
        borough_dict[each_borough] = borough_dict[each_borough] + 1
        each_event += 1
    else:
        borough_dict['No Shooting Permit'] = borough_dict['No Shooting Permit'] + 1
        each_event += 1
for place in borough_dict:
    print(f"There were {borough_dict[place]} movies filmed in {place}")