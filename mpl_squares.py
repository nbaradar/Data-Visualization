#Aliasing in python, short hand for pyplot
import matplotlib.pyplot as plt

#x/y values of graph
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#Uses one of the style available from plt.style.available
#plt.style.use('seaborn')
#plt.style.use('fivethirtyeight')
plt.style.use('Solarize_Light2')

#Common matplotlib convention
#This function generates 1 or more plots in the same figure. 
#It returns a tuple containing a figure and axes object(s)
#figure represents the entire figure or collection of plots
#ax represents a single plot in the figure and is the variable you use most of the time
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#You can adjust visualization of all features in matplotlib
#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

#.show() opens matplotlibs viewer and displays the plot
plt.show()
