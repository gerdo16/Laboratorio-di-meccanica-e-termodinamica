import math
import numpy as np

probarray = np.array([])
data = np.loadtxt('output.txt')
# Convert into np array
data = np.array(data)

# Extract unique values
uniques, counts = np.unique(data, return_counts=True)

# Statistics
mean = np.mean(data)
std = np.std(data)

# Probabilities
probabilities = counts / len(data)


for k in range(1,4):
    totalprob = 0
    upper = mean + k*std
    lower = mean - k*std
    print(upper)
    print(lower)
    for val, prob in zip(uniques, probabilities):
        if val <= upper and val>= lower:
            totalprob += prob
    print(totalprob)
        
    np.append(probarray, totalprob)
