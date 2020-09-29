import csv
from datetime import datetime #from global python

open_dv = open("death_valley_2018_simple.csv", "r") #open dv

open_sitka = open("sitka_weather_2018_simple.csv", "r") #open sitka

csv_dv = csv.reader(open_dv, delimiter= ",") #contents of dv

csv_sitka = csv.reader(open_sitka, delimiter= ",") #contents of sitka

# example of getting the "next" function to skip reading the first line
header_row_dv = next(csv_dv)

header_row_sitka = next(csv_sitka)

#automatic indexing using enumerate function
for index, column_header in enumerate(header_row_dv):
    if column_header == 'TMAX': 
        high_dvindex = index
        print("death valley high", high_dvindex, column_header)
    if column_header == 'TMIN':
        low_dvindex = index
        print("death valley low", low_dvindex, column_header)
    if column_header == 'DATE':
        date_dvindex = index
        print("death valley date", date_dvindex, column_header)

for index, column_header in enumerate(header_row_sitka): 
    if column_header == 'TMAX':
        high_sitkaindex = index
        print("sitka high", high_sitkaindex, column_header)
    if column_header == 'TMIN':
        low_sitkaindex = index
        print("sitka low", low_sitkaindex, column_header)
    if column_header == 'DATE':
        date_sitkaindex = index
        print("sitka date", date_sitkaindex, column_header)


#make lists to append to
highs_dv = []
dates_dv = []
lows_dv = []
highs_sitka = []
dates_sitka = []
lows_sitka = []

#appending all of the automatic index values to the lists we just created
for row in csv_dv:
    try:
        high_dv = row[high_dvindex]
        low_dv = row[low_dvindex]
        date_dv = datetime.strptime(row[date_dvindex],'%Y-%m-%d')
    except ValueError:
        pass 
        print("Missing data for:", date_dv)
    else:
        highs_dv.append(high_dv)
        lows_dv.append(low_dv)
        dates_dv.append(date_dv) #append the date to the list

for row in csv_sitka:
    try:
        high_sitka = row[high_sitkaindex]
        low_sitka = row[low_sitkaindex]
        date_sitka = datetime.strptime(row[date_sitkaindex],'%Y-%m-%d')
    except ValueError:
        pass
        print("Missing data for:", date_sitka)
    else:
        highs_sitka.append(high_sitka)
        lows_sitka.append(low_sitka)
        dates_sitka.append(date_sitka) #append the date to the list

import matplotlib.pyplot as plt #import the graph library as plt, an alias, plot creates a graph
print(highs_sitka [360:365])
print(lows_sitka [360:365])
print(dates_sitka [360:365])

#figure is a plt subplot
fig, a = plt.subplots(2)

#adding dates lists to plot
a[0].plot(dates_sitka, highs_sitka, c='red') 
a[0].plot(dates_sitka, lows_sitka, c='blue') 

a[0].fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)

a[1].plot(dates_dv, highs_dv, c='red') 
a[1].plot(dates_dv, lows_dv, c='blue') 

a[1].fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.1)

#fills the gap between both plots

#chart title
a[0].set_title("Sitka, AK", fontsize=16)
a[1].set_title("Death Valley, CA", fontsize=16)

#the call to fig.autofmt_xdate labels diagonally to prevemt them from overlapping.
fig.autofmt_xdate()

#print statement of subplots
plt.show()
