class Solution:
    def isValid(self, s: str) -> bool:
        d={')': '(', ']': '[', '}': '{'}
        f=[]
        if len(s)<2:
            return False
        for i in s:
            if i in d.values():
                f.append(i)
            elif i in d:
                if f and d[i]==f[-1]:
                    f.pop()
                else:
                    return False
            else:
                return False
        if f:
            return False
        return True