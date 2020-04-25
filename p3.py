inputs = [1.1, 1.3, -2, 2]

weights = [[2, 0.2, 5, 2],
           [2.1, 2, 1.5, -2],
           [2, 1.3, 5, 3.1]]

biases = [0.2, 3, -2]

output = []

for nn_weights, nn_biases in zip(weights, biases):
    product = 0

    for nn_inputs, nn_w in zip(inputs, nn_weights):
        product += nn_inputs*nn_w

    output.append(product + nn_biases)

print(output)
