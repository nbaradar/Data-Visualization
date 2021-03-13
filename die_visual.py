from die import Die

#Create a D6
d6 = Die()

#Make some rolls, and store them in a list
results = []
for roll_num in range(100):
    result = d6.roll()
    results.append(result)

print(results)    