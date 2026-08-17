class Solution:
    def climbStairs(self, n: int) -> int:
        mem={}

        def dfs(n):
            if n<0:
                return 0
            if n==0:
                return 1
            if n in mem:
                return mem[n]
            mem[n]=dfs(n-1)+dfs(n-2)
            return mem[n]
        
        return dfs(n)