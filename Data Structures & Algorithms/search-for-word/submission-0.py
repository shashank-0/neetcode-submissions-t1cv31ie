class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        mr,mc=len(board),len(board[0])
        path=set()

        def dfs(r,c,l):
            if l==len(word):
                return True
            if (r<0 or c<0 or r>=mr or c>=mc or board[r][c]!=word[l] or (r,c) in path):
                return False
            
            path.add((r,c))
            res = (dfs(r,c+1,l+1) or dfs(r,c-1,l+1) or dfs(r+1,c,l+1) or dfs(r-1,c,l+1))
            path.remove((r,c))
            return res
        
        for i in range(mr):
            for j in range(mc):
                if dfs(i,j,0):
                    return True
        return False