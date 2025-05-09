def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    # Extract elements from 2x2 matrix
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    
    # Calculate the trace (sum of diagonal elements)
    trace = a + d

    # Calculate the determinant (ad - bc)
    determinant = a * d - b * c

    # Compute discriminant for the quadratic characteristic equation
    discriminant = trace ** 2 - 4 * determinant

    # Use quadratic formula to find eigenvalues
    lambda_1 = (trace + discriminant ** 0.5) / 2
    lambda_2 = (trace - discriminant ** 0.5) / 2

    # Return eigenvalues sorted by default order
    return [lambda_1, lambda_2]


if __name__ == "__main__":
    matrix = [[1, 2], [3, 4]]
    print(calculate_eigenvalues(matrix))
