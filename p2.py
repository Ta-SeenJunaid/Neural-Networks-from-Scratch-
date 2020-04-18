inputs = [1.1, 1.3, -2, 2]

weight1 = [2, 0.2, 5, 2]
weight2 = [2.1, 2, 1.5, -2]
weight3 = [2, 1.3, 5, 3.1]

bias1 = 0.2
bias2 = 3
bias3 = -2

output = [inputs[0]*weight1[0] + inputs[1]*weight1[1] + inputs[2]*weight1[2] + inputs[3]*weight1[3] + bias1,
          inputs[0]*weight2[0] + inputs[1]*weight2[1] + inputs[2]*weight2[2] + inputs[3]*weight2[3] + bias2,
          inputs[0]*weight3[0] + inputs[1]*weight3[1] + inputs[2]*weight3[2] + inputs[3]*weight3[3] + bias3]

print(output)
