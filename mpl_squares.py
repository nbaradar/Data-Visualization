import matplotlib.pyplot as plt

#create a list called square
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()