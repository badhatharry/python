import matplotlib.pyplot as plt
import numpy as np
import csv
from numpy import *
from scipy.interpolate import *

x = []
y = []

with open('kalo_cropped.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

#p1 = polyfit(x, y, 1)
#print(p1)

plt.plot(x, y,'o' ,label='Heizkurve')
#plt.plot(x, polyval(p1,x))

plt.title('Kalorimeterkurve\n400g Wasser')
plt.ylabel('Temperatur T/K')
plt.xlabel('Zeit t/s')
plt.show()
