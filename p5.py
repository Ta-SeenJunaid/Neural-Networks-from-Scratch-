import numpy as np
from data_file_1 import spiral_data

X, y = spiral_data(100, 3)


class LayerDense:

    def __init__(self, n_inputs, n_neurons):
        self.weight = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.bias = np.zeros((1, n_neurons))

    def forward(self, inputs):
        return np.dot(inputs, self.weight) + self.bias


def relu_activation(inputs):
    return np.maximum(0,inputs)


layer1 = LayerDense(2, 5)

layer1_output = layer1.forward(X)
layer1_activation_output = relu_activation(layer1_output)

print(layer1_activation_output)