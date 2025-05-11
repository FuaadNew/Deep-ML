import numpy as np

class Diagonal:
    def __init__(self, x):
        self.x = x

    def make_diagonal(self):
        # Your code here
        res = [[0 for _ in range(len(self.x))] for _ in range(len(self.x))]

        for i in range(len(self.x)):
            res[i][i] = self.x[i]
        return res

print(Diagonal(np.array([1, 2, 3])).make_diagonal())
