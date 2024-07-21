import numpy as np
from statistics import mean

def bestfit(x, y):
    numerator = mean(x * y) - mean(x) * mean(y)
    denominator = mean(x ** 2) - mean(x) ** 2
    m = numerator / denominator
    b = mean(y) - m * mean(x)
    return m, b

c = []
l = []

with open("trainingdata.txt") as file:
    for line in file:
        fields = line.split(',')
        x_value = float(fields[0])
        y_value = float(fields[1][:4])
        if x_value <= 4.00:
            c.append(x_value)
            l.append(y_value)

c = np.array(c)
l = np.array(l)

m, b = bestfit(c, l)

n = float(input("Enter a value: "))
if n > 4.00:
    print(8.00)
else:
    print(m * n + b)
