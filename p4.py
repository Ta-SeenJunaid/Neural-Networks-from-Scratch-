import numpy as np

np.random.seed(0)

X = [[1, 2.3, 4, 2.5],
     [2, 3.7, 0.2, 4.3],
     [1, 3.2, 2, 2.6]]


class LayerDense:

    def __init__(self, n_inputs, n_neurons):
        self.weight = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.bias = np.zeros((1, n_neurons))

    def forward(self):
        pass


