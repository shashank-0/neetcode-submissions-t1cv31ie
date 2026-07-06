class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0

        rm,cm=len(grid),len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r>=rm or c>=cm or grid[r][c]=="0":
                return
            if grid[r][c]=="1":
                grid[r][c]="0"
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        
        for r in range(rm):
            for c in range(cm):
                if grid[r][c]=="1":
                    res+=1
                    dfs(r,c)
        
        return res