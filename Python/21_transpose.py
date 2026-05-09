def transpose(matrix):
    #We Get the number of rows and columns from the original
    rows = len(matrix)
    cols = len(matrix[0])
    
    #Create a new empty matrix with flipped dimensions
    #This creates a structure like [[None, None], [None, None], [None, None]]
    transposed = [[None for _ in range(rows)] for _ in range(cols)]
    
    #We fill the new matrix by swapping the indices
    for r in range(rows):
        for c in range(cols):
            #The value at [r][c] moves to [c][r]
            transposed[c][r] = matrix[r][c]
            
    return transposed
transpose([[1, 2, 3], [4, 5, 6]]) #should return [[1, 4], [2, 5], [3, 6]]
transpose([[1, 2], [3, 4], [5, 6], [7, 8]]) #should return [[1, 3, 5, 7], [2, 4, 6, 8]]
