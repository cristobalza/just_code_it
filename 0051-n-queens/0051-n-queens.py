'''
Given n : integer, R: a baord :2D of nxn size that shows all possible Q positiionion without inteferring one with anohter . the number Qs is the same as n

n = 4
  0 1 2 3
[[. Q . . ]]
 [. . . Q ]
 [Q . . . ]
 [. . Q . ]]

backtracking solution because it can show every sinlge position

[[* Q * * ]]
 [* * * Q ]
 [Q * * * ]
 [* * Q * ]]
 
 
 n == 0 solution
 
 mark candidate : baord[r][c] = Q , then do all marking with *
 


'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_hset = set()
        postive_diag_hset = set()
        negative_diag_hset = set()
        
        
        board = [['.'] * n for _ in range(n)]
        res = []
        
        def backtrack(r):
            if r == n:
                temp = ["".join(row) for row in board]
                res.append(temp)
                return
            else:
                for c in range(n):
                    if c not in col_hset and (r + c) not in postive_diag_hset and (r - c) not in negative_diag_hset:
                        col_hset.add(c)
                        postive_diag_hset.add((r + c))
                        negative_diag_hset.add((r - c))
                        board[r][c] = 'Q'

                        backtrack(r + 1)

                        col_hset.remove(c)
                        postive_diag_hset.remove((r + c))
                        negative_diag_hset.remove((r - c))
                        board[r][c] = '.'
        backtrack(0)
        return res
                    
                    