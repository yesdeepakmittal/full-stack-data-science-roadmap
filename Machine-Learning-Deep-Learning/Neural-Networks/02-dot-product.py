import numpy as np

inp = [1, 2, 3, 4]
wts = [1, 2, 3, 4]
bias = 2

print(np.dot(wts,inp) + bias)

inp = [1, 2, 3, 4]

wts = [[1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4]]
biases = [1,1,1]

layer_outputs = np.dot(wts, inp) + biases

print(layer_outputs)
