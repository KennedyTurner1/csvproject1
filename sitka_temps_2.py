#take high temps and the date and plot them

import csv
from datetime import datetime #from global python

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ",") #use the delimiter function

header_row = next(csv_file)
'''
print(header_row) #the next function skips reading the first line

for index, column_header in enumerate(header_row): 
    print(index, column_header)
'''
highs = []
dates = []

''' #example of getting a date
x = datetime.strptime('2018-07-01', '%Y-%m-%d') #want to convert to date format instead of string format from the csv file
print(x)
'''

for row in csv_file:
    highs.append(int(row[5])) #gets the index value
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(the_date)

import matplotlib.pyplot as plt #import the graph library as plt, an alias, plot creates a graph

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.title("Daily High Temps, July 2018", fontsize=16)
plt.xlabel("") 
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both",labelsize=16)

fig.autofmt_xdate()

plt.plot()
