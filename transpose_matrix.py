from typing import List
def transpose_matrix(a: List[List[int|float]]) -> List[List[int|float]]:
	#rows become columns
    #columns become rows 
    res = []
    for j in range(len(a[0])): #for every column  
        row = []
        for i in range(len(a)):
            #for every row 
            row.append(a[i][j])
        res.append(row)
    return res

print(transpose_matrix([[1,2],[3,4],[5,6]]))