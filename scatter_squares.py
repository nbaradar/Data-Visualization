import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()

#plots a single point at the passed in coordinates
#The s argument sets the size of the dots used to draw the graph
ax.scatter(2, 4, s=200)

#Set Chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Sqaure of Value", fontsize = 14)

#Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize = 14)

plt.show()