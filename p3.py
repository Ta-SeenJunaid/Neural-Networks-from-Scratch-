import numpy as np

inputs = [1.1, 1.3, -2, 2]

weights = [[2, 0.2, 5, 2],
           [2.1, 2, 1.5, -2],
           [2, 1.3, 5, 3.1]]

biases = [0.2, 3, -2]

output = np.dot(weights, inputs) + biases

print(output)

