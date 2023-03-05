class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        area, s_r, e_r, s_c, e_c, res, i = m * n, 0, m,  0, n, [], 0
        check = lambda i : i < area
        while check(i):
            # right
            for c in range(s_c, e_c):
                if check(i):
                    res.append(matrix[s_r][c])
                    i += 1
                else:
                    break
            s_r += 1
            
            # down
            for r in range(s_r, e_r):
                if check(i):
                    res.append(matrix[r][e_c-1])
                    i += 1
                else:
                    break
            e_c -= 1
            
            # left
            for c in range(e_c - 1, s_c - 1, -1): # 1, 0-1
                if check(i):
                    res.append(matrix[e_r-1][c])
                    i += 1
                else:
                    break
            e_r -= 1
            
            # up 
            for r in range(e_r - 1, s_r - 1, -1):
                if check(i):
                    res.append(matrix[r][s_c])
                    i += 1
                else:
                    break
            s_c += 1
        return res