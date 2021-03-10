#Aliasing in python, short hand for pyplot
import matplotlib.pyplot as plt

#create a list called square
squares = [1, 4, 9, 16, 25]

#Common matplotlib convention
#This function generates 1 or more plots in the same figure. 
#It returns a tuple containing a figure and axes object(s)
#figure represents the entire figure or collection of plots
#ax represents a single plot in the figure and is the variable you use most of the time
fig, ax = plt.subplots()
ax.plot(squares)

#.show() opens matplotlibs viewer and displays the plot
plt.show()