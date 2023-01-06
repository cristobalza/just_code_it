class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.n, self.m = len(matrix[0]), len(matrix)
        
        self.transpose(matrix)
        
        self.reflection(matrix)
        
    def transpose(self, matrix):
        
        for r in range(self.m):
            for c in range(r, self.n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
    def reflection(self, matrix):
        
        for r in range(self.m):
            for c in range(self.n // 2):
                matrix[r][c], matrix[r][-c-1] = matrix[r][-c-1], matrix[r][c]