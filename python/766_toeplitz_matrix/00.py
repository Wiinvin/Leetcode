class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return True
        
        ## loop through columns -> upper right triangle
        for j in range(len(matrix[0])):
            it = 0
            i = 0
            k = j
            val = matrix[i][j]
            while k < len(matrix[0]) and i < len(matrix):
                if matrix[i][k] != val:
                    return False
                it += 1
                i += 1
                k += 1

        
        ## loop through rows -> lower left triangle
        val = None
        for i in range(1, len(matrix)):
            it = 1
            k = i
            j = 0
            val = matrix[i][j]
            while k < len(matrix) and j < len(matrix[0]):
                if matrix[k][j] != val:
                    return False
                it += 1
                k += 1
                j += 1
        
        return True

        
