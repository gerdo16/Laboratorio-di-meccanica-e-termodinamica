import numpy as np

data = np.loadtxt('misureSecondaSuperficie.txt')

l = data[:, 7]
min = min(l)
max = max(l)

l_fin = (min+max)/2
delta_l = (max-min)/2

print(l_fin, delta_l)

print("-- PRIMA SUPERFICIE --")
print("l1 = 12 +/- 2")
print("l2 = 13.25 +/- 2.25")
print("l3 = 13.50 +/- 1.50")
print("l4 = 16.50 +/- 2.00")
print("l5 =  17.90 +/- 1.90")
print("l6 = 23.00 +/- 3.00")
print("l7 = 24.00 +/- 4.00")
print("l8 = 31.75 +/- 3.75")

print("-- SECONDA SUPERFICIE --")
print("l1 = 20.75 +/- 1.25")
print("l2 = 24.25 +/- 2.25")
print("l3 = 27.00 +/- 1.00")
print("l4 = 28.50 +/- 2.50")
print("l5 = 32.00 +/- 2.50")
print("l6 = 35.25 +/- 2.25")
print("l7 = 38.50 +/- 2.50")
print("l8 = 42.50 +/- 4.50")
