def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
    res = []
    m = len(a[0])
    if m != len(b):
        return -1

    for i in range(len(a)):
        val = 0
        for j in range(len(b)):
            val += a[i][j] * b[j] 
        res.append(val)
    return res

print(matrix_dot_vector([[1, 2, 3], [4, 5, 6]], [1, 2, 3]))
