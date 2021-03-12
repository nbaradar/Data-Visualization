from random import choice

class RandomWalk:
    """A class to generate random walks"""

    #In python, you can set the default value of a parameter this way
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points
        
        #All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""
        
        #Keep taking steps until the walk reaches desired length
        while len(self.x_values) < self.num_points:
            
            #Decide which direction to go 
            x_direction = choice([1, -1])
            #and how far to go in that direction
            x_distance = choice([0, 1, 2, 3, 4])
            #positive means right, negative means left, 0 means vertical
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0,1,2,3,4])
            #positive means up, negative means down, 0 means horizontal
            y_step = y_direction * y_distance

            #Reject moves that go no where
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the new position
            #In python, using -1 in an array brings you to the end of the array. Same goes for strings
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    
