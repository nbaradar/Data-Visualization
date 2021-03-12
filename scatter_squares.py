import matplotlib.pyplot as plt

#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
x_values = range(1, 1001)

#The power operator 'x**2' has the same built in function as pow(x, 2)
#In python, "list comprehension" allows shorter syntax to generate new lists based off old ones 
# === Example WITHOUT List Comprehension ===
#   newlist = []
#   for x in fruits:
#       if "a" in x:
#           newlist.append(x)
# === Example WITH List Comprehension ===
#   newlist = [x for x in fruits if "a" in x]
# === The Syntax ===
#   newlist = [expression for item in iterable if condition == True]
y_values = [x**2 for x in x_values]

test_x = range(1, 1001)
test_y = [(x**2)+(x*20) for x in test_x]

plt.style.use('seaborn')
fig, ax = plt.subplots()

#plots a single point at the passed in coordinates
#The s argument sets the size of the dots used to draw the graph
#The c argument sets the color of the dots used to draw the graph. You can also use rgb tuple. lower = darker; ex. (0, 0.8, 0)
ax.scatter(x_values, y_values, c='red', s=10)

#Colormaps are a series of colors in a gradient. Used to emphasize pattern in data
#You must tell pyplot to assign a color to each point in the data set
ax.scatter(test_x, test_y, c=test_y, cmap=plt.cm.Blues, s=10)

#Set Chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Sqaure of Value", fontsize = 14)

#Set the range for each axes
#The axis method requires 4 values: Min/Max of X-axis and Min/Max of Y-axis
ax.axis([0, 1100, 0, 1100000])

#Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize = 14)

#This changes the display format of the axes from scientific notation to standard formatting.
#Matplotlib uses scientific notation as default. See: matplotlib.axes.Axes.ticklabel_format
ax.ticklabel_format(style='plain')

plt.show()