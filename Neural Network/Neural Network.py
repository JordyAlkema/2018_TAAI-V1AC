import json


def dot(l_matrix, r_matrix):
    dot_result = []
    result_row = []

    # Make sure it has the correct structure, otherwise give it the correct structure
    if not hasattr(r_matrix[0], '__len__'):
        r_matrix = [r_matrix]

    # Make sure it has the correct structure, otherwise give it the correct structure
    if not hasattr(l_matrix[0], '__len__'):
        l_matrix = [l_matrix]

    for l in range(len(r_matrix[0])):
        result_row.append(0)

    # Copy otherwise all rows will become references and multiplication will go wrong.
    for l in range(len(l_matrix)):
        dot_result.append(result_row.copy())

    # loop over rows from l_matrix
    for l in range(len(l_matrix)):
        # Loop over columns of r_matrix
        for r in range(len(r_matrix[0])):
            # Loop over rows from r_matrix
            for rr in range(len(r_matrix)):
                dot_result[l][r] += l_matrix[l][rr] * r_matrix[rr][r]

    return dot_result


# Configuration
file_path = "example.json"
input_vector = [1, 1, 1, 1, 1]

file = open(file_path, 'r')
json_data = json.load(file)

matrices = []

# Parse JSON data
for layer in json_data:
    matrix = []
    weights = json_data[layer]["weights"]
    output_layer_size = int(json_data[layer]["size_out"])

    for node_weights in weights:
        node = weights[node_weights]

        # Create a new vector with the length of the output size
        list_weights = [0] * int(output_layer_size)

        for weight in node:
            list_weights[int(weight) - 1] = float(node[weight])

        matrix.append(list_weights)
    matrices.append(matrix)

result = None

if len(matrices) == 1:
    result = dot(input_vector, matrices[0])
else:
    n_matrices = len(matrices)

    prev_result = dot(matrices[-2], matrices[-1])

    for i in range(n_matrices - 2, 0):
        prev_trans_matrix = dot(matrices[i], prev_result)

    result = dot(input_vector, prev_result)

print(result)
