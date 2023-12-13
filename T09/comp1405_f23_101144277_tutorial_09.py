#Tutorial 9 by Prayanshu Narayan (101144277)
def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return []
    
    result_matrix = []
    for i in range(len(matrix1)):
        result_row = []
        for j in range(len(matrix1[0])):
            result_row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(result_row)
    
    return result_matrix

def main():
    matrix1 = [[1, 3], [1, 0], [1, 2],]
    matrix2 = [[0, 0], [7, 5], [2, 1]]
    print(matrix_addition(matrix1, matrix2))
    
main()