import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep making new walks as long as the program is active
while True:
    #Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    #Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()

    #Lets create a color gradient so it's easy to see the order of the walk from light to dark
    #Because the points are plotted in order, the list can just contain 0-4999
    point_numbers = range(rw.num_points)

    #We then pass the list in for "c" 
    #We select the colormap gradient by passing value into cmap.
    #Passing 'none' into 'edgecolors' removes the black outline around each point.
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

    #We can also plot the first and last points seperately to emphasize them
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Remove the axes to minimize distractions from the path
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    #If the viewer exits, wait for user input
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
