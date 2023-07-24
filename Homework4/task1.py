#Напишите функцию для транспонирования матрицы


def matrix_transp(matrix_input:list)->list:
    matrix_res = [[matrix_input[j][i] for j in range(len(matrix_input))] for i in range(len(matrix_input[0]))]
    return matrix_res


matrix = [[2, 1, 3], [3, 1, 5]]
transp_matrix = matrix_transp(matrix)
print(transp_matrix)