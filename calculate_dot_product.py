import numpy as np

class DotProduct:
    def __init__(self, vec1, vec2):
        self.vec1 = vec1
        self.vec2 = vec2

    def calculate_dot_product(self) -> float:
        """
        Calculate the dot product of two vectors.
        Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
        """
        # Your code here
        return np.dot(self.vec1, self.vec2)

print(DotProduct(np.array([1, 2, 3]), np.array([4, 5, 6])).calculate_dot_product())