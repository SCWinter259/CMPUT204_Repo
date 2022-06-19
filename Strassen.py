# Assumptions for Strassen's algorithm:
# 1. Always be two a times a matrices multiplied together
# 2. If the matrices are not a times a, you can fill
# them with additional 0 rows or columns until they are a times a

# Sample 2x2 matrices
two_matrix_1 = [[1, 3], [2, 4]]
two_matrix_2 = [[2, 3], [1, 4]]

def basicMatrixMultiplier(two_matrix_1, two_matrix_2):
    '''
    This function takes in 2 2x2 matrices
    and multiply them
    '''
    # creating an empty result matrix
    result_matrix = []
    for i in range(len(two_matrix_1)):
        row = []
        for j in range(len(two_matrix_1)):
            row.append(None)
        result_matrix.append(row)
    
    # actual calculations
    # fill the rows
    for i in range(len(result_matrix)):
        #fill each column in row
        for j in range(len(result_matrix)):
            element = 0
            # each element calculation
            for k in range(len(two_matrix_1)):
                element = element + (two_matrix_1[i][k] * two_matrix_2[k][j])
            result_matrix[i][j] = element

    return result_matrix

print(basicMatrixMultiplier(two_matrix_1, two_matrix_2))