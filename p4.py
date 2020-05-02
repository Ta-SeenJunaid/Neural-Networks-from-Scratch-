import numpy as np

inputs = [[1, 2.3, 4, 2.5],
     [2, 3.7, 0.2, 4.3],
     [1,3.2, 2, 2.6]]

weights = [[2, 0.2, 5, 2],
           [2.1, 2, 1.5, -2],
           [2, 1.3, 5, 3.1]]

biases = [0.2, 3, -2]

output = np.dot(inputs,np.array(weights).T) + biases

print(output)