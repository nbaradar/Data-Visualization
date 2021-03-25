import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_07-2018_simple.csv'

#Open the file and assign the resulting file object to f
#"with" keyword is used when working with unmanaged resources (like file streams)
with open(filename) as f:
    #create a reader object
    reader = csv.reader(f)
    #The next() function returns the next line in the file
    header_row = next(reader)

    #Get the high temperatures for this file
    highs = []
    dates = []

    for row in reader:
        high = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        highs.append(high)
        dates.append(current_date)

    plt.style.use('seaborn')

    fig, ax = plt.subplots()

    ax.plot(dates, highs, linewidth=2, c='red')

    ax.set_title("Daily high temperatures, July 2018", fontsize=24)
    ax.set_xlabel("Day", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)


    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

   # print(highs)
"""     #enumerate returns both the index of each item and the value of each item as you loop through the list
    for index, column_header in enumerate(header_row):
        #You can seperate multiple arguments with print(), python will automatically add a space between them
        print(index, column_header) """

    