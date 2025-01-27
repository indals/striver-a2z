class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[i][0] = '#'
                    matrix[0][j] = '#'
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]=='#' or  matrix[0][j]=='#' :
                    matrix[i][j]= 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='#':
                    matrix[i][j]= 0
