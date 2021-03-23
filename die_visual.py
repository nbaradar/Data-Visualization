from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout


#Create a D6
d6 = Die(6)
d6_2 = Die(6)

#Create a D10
d10 = Die(10)

#Make some rolls, and store them in a list
results = []
results2D6 = []
resultsD6D10 = []

for roll_num in range(1000):
    result = d6.roll()
    results.append(result) 

for roll_num in range(1000):
    result = d6.roll() + d6_2.roll()
    results2D6.append(result)

#!TIP! -- In python you can use an "_" in a numeric literal to create visual seperators, like a "," in everyday language. 
for roll_num in range(50_000):
    result = d6.roll() + d10.roll()
    resultsD6D10.append(result)

#Analyze the results. Return the frequency of the rolls using .count() and store in a list
#.count() lets you pass in any type to search for
largestPossibleRoll = d6.num_sides + d10.num_sides;
frequencies = []
""" for side in range(1, d6.num_sides+1):
    frequency = results.count(side)
    frequencies.append(frequency) """

for side in range(2, largestPossibleRoll+1):
    frequency = resultsD6D10.count(side)
    frequencies.append(frequency)

#Visualize the results by creating a histogram using plotly
#The xvalues along the bottom of the graph will be the number of sides
x_values = list(range(2, largestPossibleRoll+1))
#Bar() represents a data set that will be formatted as a bar chart
#this class needs list of xvals and yvals
#It is wrapped around brackets because a data set can have multiple elements
data = [Bar(x=x_values, y=frequencies)]

#These dictionary entries store the axis configurations
#the dtick setting controls the spacing between tick marks on the x-axis
x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title':'Frequency of Result'}

#derive the title from the num of sides and amount of rolls
my_title = 'Results of rolling two D' + str(d6.num_sides)+ ' ' + str(sum(frequencies))+ ' times'
my_title2 = 'Results of rolling a D6 and D10 ' + str(sum(frequencies))+ ' times'
#Layout() returns an object that specifies the layout and configs of the graph
#We set the title, and xaxis/yaxis configs
my_layout = Layout(title = my_title2, xaxis = x_axis_config, yaxis = y_axis_config)

#plot() needs a dictionary containing the data to plot and layout objects. Also accepts filename to store graph
offline.plot({'data':data, 'layout':my_layout,}, filename='d6d10.html')

#print(results)   
print(frequencies)
