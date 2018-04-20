import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('kalorimeter.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y,'bo' ,label='Heizkurve')

plt.title('Kalorimeterkurve\n400g Wasser')
plt.ylabel('Temperatur T/K')
plt.xlabel('Zeit t/s')
plt.show()
