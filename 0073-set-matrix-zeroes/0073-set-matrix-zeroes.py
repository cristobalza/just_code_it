class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        stack = []
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    stack.append((r,c))
        
        while stack:
            r, c = stack.pop()
            self.helper(matrix, r, c, m, n)
            
    def helper(self, matrix, r, c, m, n):
        for i in range(m):
            matrix[i][c] = 0
        for j in range(n):
            matrix[r][j] = 0
        
            