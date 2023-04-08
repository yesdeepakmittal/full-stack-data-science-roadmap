'''
NN with 4 input nodes & 3 Output Nodes

---
- Number of Weight vector = Number of Output Nodes
- Weight Vector Length = Number of Input Nodes
- Each wt in Weight Vector represents associated wt towards Output Node
'''
inputs = [1, 2, 3, 4]

weights1 = [0.1, 0.2, -0.3, 0.4]
weights2 = [0.1, 0.2, -0.3, 0.4]
weights3 = [0.1, 0.2, -0.3, 0.4]

bias1 = 0.2
bias2 = 0.3
bias3 = 0.5

output_node_one = output_node_two = output_node_three = 0

for i,v in enumerate(inputs):
    output_node_one += inputs[i] * weights1[i]
    output_node_two += inputs[i] * weights2[i]
    output_node_three += inputs[i] * weights3[i]
    
output_node_one += bias1
output_node_two += bias2
output_node_three += bias3

print(output_node_one,output_node_two,output_node_three)