def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    res = []
    if mode == 'column':
        for j in range(len(matrix[0])):
            col_sum = 0
            for i in range(len(matrix)):
                col_sum+= matrix[i][j]
            col_sum = col_sum // len(matrix[0])
            res.append(col_sum)
        return res
            
    else:
        for i in range(len(matrix)):
            row_sum = 0
            for j in range(len(matrix[0])):
                row_sum+=matrix[i][j]
            row_sum = row_sum//(len(matrix))
            res.append(row_sum)

        return res
