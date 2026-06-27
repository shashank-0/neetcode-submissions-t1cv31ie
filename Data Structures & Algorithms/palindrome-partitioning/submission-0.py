class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        sub=[s[0]]

        def ispal(a):
            for i in a:
                j,k=0,len(i)-1
                while j<k:
                    if i[j]!=i[k]:
                        return False
                    j+=1
                    k-=1
            return True

        def back(i,sub):
            if i==len(s):
                if ispal(sub):
                    res.append(sub[:])
                return
            sub.append(s[i])
            back(i+1,sub)
            sub.pop()
            sub[-1]+=s[i]
            back(i+1,sub)
            sub[-1] = sub[-1][:-1]
        
        back(1,sub)
        return res