import csv
from datetime import datetime #from global python

open_file = open("death_valley_2018_simple.csv", "r") #change the file to match death valley instead of sitka

csv_file = csv.reader(open_file, delimiter= ",") #use the delimiter function

# example of getting the "next" function to skip reading the first line
header_row = next(csv_file)

'''
print(header_row) 

for index, column_header in enumerate(header_row): 
    print(index, column_header)
'''
highs = []
dates = []
lows = []

''' #example of getting a date
x = datetime.strptime('2018-07-01', '%Y-%m-%d') #want to convert to date format instead of 
                                                #string format from the csv file
print(x)
'''

for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d') #strip out time
    except ValueError:
        pass
        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date) #append the date to the list

import matplotlib.pyplot as plt #import the graph library as plt, an alias, plot creates a graph

#figure is a plt subplot
fig = plt.figure()

#adding dates lists to plot
plt.plot(dates, highs, c="red", alpha=0.5) 
plt.plot(dates, lows, c="blue", alpha=0.5)

#chart title
plt.title("Daily High and Low Temps - 2018\nDeath Valley", fontsize=16)

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
