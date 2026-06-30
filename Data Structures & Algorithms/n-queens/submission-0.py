class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]

        col=set()
        rd=set()
        ld=set()

        def back(i,sub):
            if i==n:
                res.append(sub[:])
            for j in range(n):
                if j in col or (i-j) in rd or (i+j) in ld:
                    continue
                col.add(j)
                rd.add(i-j)
                ld.add(i+j)
                sub.append(("."*j)+("Q")+("."*(n-j-1)))
                back(i+1,sub)
                sub.pop()
                col.remove(j)
                rd.remove(i-j)
                ld.remove(i+j)
        
        back(0,[])
        return res
