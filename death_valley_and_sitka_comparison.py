import csv
from datetime import datetime #from global python

open_dv = open("death_valley_2018_simple.csv", "r") #change the file to match death valley instead of sitka

open_sitka = open("sitka_weather_2018_simple.csv", "r")

csv_dv = csv.reader(open_dv, delimiter= ",") #use the delimiter function

csv_sitka = csv.reader(open_sitka, delimiter= ",") #use the delimiter function

# example of getting the "next" function to skip reading the first line
header_row_dv = next(csv_dv)

header_row_sitka = next(csv_sitka)

'''
print(header_row) 

for index, column_header in enumerate(header_row): 
    print(index, column_header)
'''
highs_dv = []
dates_dv = []
lows_dv = []
highs_sitka = []
dates_sitka = []
lows_sitka = []

''' #example of getting a date
x = datetime.strptime('2018-07-01', '%Y-%m-%d') #want to convert to date format instead of 
                                                #string format from the csv file
print(x)
'''

for row in csv_dv:
    try:
        high_dv = int(row[4])
        low_dv = int(row[5])
        current_date_dv = datetime.strptime(row[2], '%Y-%m-%d') #strip out time
    except ValueError:
        pass
        print(f"Missing data for {current_date_dv}")
    else:
        highs_dv.append(high_dv)
        lows_dv.append(low_dv)
        dates_dv.append(current_date_dv) #append the date to the list

for row in csv_sitka:
    try:
        high_sitka = int(row[4])
        low_sitka = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d') #strip out time
    except ValueError:
        pass
        print(f"Missing data for {current_date}")
    else:
        highs_sitka.append(high_sitka)
        lows_sitka.append(low_sitka)
        dates_sitka.append(current_date) #append the date to the list

import matplotlib.pyplot as plt #import the graph library as plt, an alias, plot creates a graph

#figure is a plt subplot
fig, ax = plt.subplots(2,2)

#adding dates lists to plot
ax[0].plot(dates_dv, highs_dv, c = 'red', alpha = 0.5) #first plot, first line plot one axis at a time
ax[0].plot(dates_dv, lows_dv, c = 'blue', alpha = 0.5) # first plot, second line
ax[1].plot(dates_sitka, highs_sitka, c = 'red', alpha = 0.5) #second plot, first line
ax[1].plot(dates_sitka, lows_sitka, c = 'blue', alpha = 0.5) #second plot, second line

#chart title
ax[0].title("High and Low Temp. Comparison: Sitka, AK", fontsize=16)
ax[1].title("Death Valley, CA", fontsize=16)

#label for the x axis
plt.xlabel("", fontsize=12) 

#fills the gap between both plots
ax[0].fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.1)
ax[1].fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)

#label for the y axis
plt.ylabel("Temperature (F)", fontsize=16)

#change the appearance of ticks, tick labels, gridlines
plt.tick_params(axis="both",labelsize=16)

#the call to fig.autofmt_xdate labels diagonally to prevemt them from overlapping.
fig.autofmt_xdate()

#print statement of subplots
plt.show()
