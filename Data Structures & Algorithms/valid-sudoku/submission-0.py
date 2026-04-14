class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in board:
            d={}
            for j in i:
                if j==".":
                    continue
                elif j in d:
                    return False
                else:
                    d[j]=1
        for i in range(9):
            d={}
            for j in range(9):
                if board[j][i]==".":
                    continue
                elif board[j][i] in d:
                    return False
                else:
                    d[board[j][i]]=1
        for i in range(3):
            for j in range(3):
                d={}
                for k in range(3):
                    for l in range(3):
                        if board[i*3+k][j*3+l]==".":
                            continue
                        elif board[i*3+k][j*3+l] in d:
                            return False
                        else:
                            d[board[i*3+k][j*3+l]]=1
        return True