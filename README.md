# Deep-ML: Machine Learning Exercises

This repository contains a collection of machine learning exercises and implementations. Each exercise focuses on different aspects of machine learning, from basic linear algebra operations to more complex algorithms.

## Contents

- **Linear Algebra Operations**
  - Matrix-Vector Multiplication (`matrix_dot_vector.py`): Implementation of matrix-vector dot product with input validation
  - Matrix Transposition (`transpose_matrix.py`): Implementation of matrix transposition with type hints and input validation
- **Matrix Reshaping Utility**
  - `reshape_matrix`: A utility function for reshaping 2D matrices while preserving element order

## Getting Started

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Deep-ML.git
cd Deep-ML
```

2. Ensure you have Python installed (Python 3.x recommended)

## Project Structure

```
Deep-ML/
├── README.md
├── matrix_dot_vector.py
├── transpose_matrix.py
└── ... (more exercises to come)
```

## Contributing

Feel free to contribute to this repository by:
- Adding new machine learning exercises
- Improving existing implementations
- Adding documentation
- Reporting issues

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# Matrix Reshaping Utility

This project provides a utility function for reshaping 2D matrices while preserving element order.

## Functionality

The `reshape_matrix` function takes a 2D matrix and a target shape as input and returns a reshaped matrix with the same elements in row-major order.

### Parameters
- `a`: A 2D list of integers or floats
- `new_shape`: A tuple of two integers (rows, cols) specifying the target shape

### Returns
- A reshaped 2D matrix if the reshape is valid
- An empty list if the reshape is invalid (total elements don't match)

### Example
```python
matrix = [[1, 2, 3], [4, 5, 6]]
new_shape = (3, 2)
result = reshape_matrix(matrix, new_shape)
# Result: [[1, 2], [3, 4], [5, 6]]
```

## Requirements
- Python 3.x
- NumPy (for type hints)

## Usage
```python
from reshape_matrix import reshape_matrix

# Example usage
matrix = [[1, 2, 3], [4, 5, 6]]
new_shape = (3, 2)
result = reshape_matrix(matrix, new_shape)
``` 