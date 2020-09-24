#took high temps from sitka alaska and plotted them using matplotlib

import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ",") #use the delimiter function

header_row = next(csv_file)
'''
print(header_row) #the next function skips reading the first line

for index, column_header in enumerate(header_row): 
    print(index, column_header)
'''
highs = []

for row in csv_file:
    highs.append(int(row[5])) #gets the index value

print(highs)

import matplotlib.pyplot as plt #import the graph library as plt, an alias, plot creates a graph

plt.plot(highs, c="red")

plt.title("Daily High Temps, July 2018", fontsize=16)
plt.xlabel("") #x - axis label empty, we have to label the x-axis (sitka_temps_2)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16) #only shows major temps

plt.show()

