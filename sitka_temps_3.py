#add the lows, plot the lows, fill in between the lines

import csv
from datetime import datetime #from global python

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ",") #use the delimiter function

header_row = next(csv_file)
'''
print(header_row) #the next function skips reading the first line

for index, column_header in enumerate(header_row): 
    print(index, column_header)
'''
highs = []
dates = []
lows = []

''' #example of getting a date
x = datetime.strptime('2018-07-01', '%Y-%m-%d') #want to convert to date format instead of string format from the csv file
print(x)
'''

for row in csv_file:
    highs.append(int(row[5])) #gets the index value
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(the_date)
    lows.append(int(row[6]))

import matplotlib.pyplot as plt #import the graph library as plt, an alias, plot creates a graph

fig = plt.figure()

plt.plot(dates, highs, c="red", alpha=.5) #alpha makes the font transparent
plt.plot(dates, lows, c="blue", alpha=.5)

#chart title
plt.title("Daily High and Low Temps - 2018", fontsize=16)

#label for the x axis
plt.xlabel("", fontsize=12) 

#fills the gap between
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#label for the y axis
plt.ylabel("Temperature (F)", fontsize=16)

#change the appearance of ticks, tick labels, gridlines
plt.tick_params(axis="both",labelsize=16)

#the call to fig.autofmt_xdate labels diagonally to prevemt them from overlapping.
fig.autofmt_xdate()

#print statement of figures
plt.show()
