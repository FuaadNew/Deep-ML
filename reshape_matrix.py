import numpy as np
from typing import list, tuple 

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	
    rows,cols = len(a),len(a[0])
    new_rows,new_cols = new_shape

    if (rows * cols) != (new_rows * new_cols):
        return []
    
    flat = []

    for r in range(rows):
        for c in range(cols):
            flat.append(a[r][c])

    res = []
    for r in range(new_rows):
        row = []
        for c in range(new_cols):
            row.append(flat[r * new_cols + c])
        res.append(row)
    return res