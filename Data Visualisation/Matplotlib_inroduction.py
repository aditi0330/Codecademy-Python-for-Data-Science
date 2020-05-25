#Basic Line Plot
from matplotlib import pyplot as plt
days = [0, 1, 2, 3, 4, 5,6]
money_spent = [10, 12, 12, 10, 14, 22, 24]
plt.plot(days, money_spent)
plt.show()

#Two plots
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
plt.plot(time, revenue)
plt.plot(time, costs)
plt.show()

#Linestyles
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
plt.plot(time, revenue, color = 'purple', linestyle = '--')
plt.plot(time, costs, color = '#82edc9', marker = 's')
plt.show()

#Axis and Labels
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)

#The minimum x-value displayed
#The maximum x-value displayed
#The minimum y-value displayed
#The maximum y-value displayed
plt.axis([0, 12, 2900, 3100])
plt.show()

#Labelling the axes
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.xlabel('Time')
plt.ylabel('Dollars spent on Coffee')
plt.title('My Last Twelve Years of Coffee Drinking')
plt.show()

#Subplots
months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]
plt.subplot(1, 2, 1)
plt.plot(temperature, months)
plt.show()

plt.subplot(1, 2, 2)
plt.plot(temperature, flights_to_hawaii)
plt.show()