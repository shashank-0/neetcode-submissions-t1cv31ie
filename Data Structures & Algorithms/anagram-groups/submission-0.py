class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a={}
        for i in strs:
            s="".join(sorted(i))
            if s not in a:
                a[s]=[i]
            else:
                a[s].append(i)
        f=[]
        for i in a.values():
            f.append(i)
        return f
