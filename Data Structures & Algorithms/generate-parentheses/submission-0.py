class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        n*=2

        def back(i,k,sub):
            if (i==n and k!=0) or k<0:
                return
            if i==n and k==0:
                res.append(sub[:])
                return
            sub+="("
            back(i+1,k+1,sub)
            sub=sub[:-1]
            sub+=")"
            back(i+1,k-1,sub)
        
        back(0,0,"")
        return res