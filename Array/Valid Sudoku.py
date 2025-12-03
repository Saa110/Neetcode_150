class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 1. ROW CHECK
        for i in board:
            d = Initialize_dict()
            for j in i:
                if j == ".":
                    continue
                if d[j] == 1:
                    return False
                else:
                    d[j] = 1
        
        # 2. COLUMN CHECK
        for j in range(9):
            d = Initialize_dict()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                
                val = board[i][j]
                if d[val] == 1:
                    return False
                else:
                    d[val] = 1
                    
        # 3. SUB-BOX CHECK
        for i in range(9):
            d = Initialize_dict()
            for j in range(9):
                row_idx = (i // 3) * 3 + (j // 3)
                col_idx = (i % 3) * 3 + (j % 3)
                
                if board[row_idx][col_idx] == ".":
                    continue
                if d[board[row_idx][col_idx]] == 1:
                    return False
                else:
                    d[board[row_idx][col_idx]] = 1

        return True

def Initialize_dict():
    d = {}
    for i in range(9):
        d[str(i+1)] = 0
    return d
