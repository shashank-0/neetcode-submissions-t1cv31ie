class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for j in t:
            if j not in dic:
                return False
            elif dic[j]==1:
                dic.pop(j)
            else:
                dic[j]-=1
        if len(dic)==0:
            return True
        else:
            return False