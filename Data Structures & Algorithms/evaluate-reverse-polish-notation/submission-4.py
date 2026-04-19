class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        t=[]
        for i in range(len(tokens)):
            if tokens[i] not in {"+", "-", "*", "/"}:
                t.append(int(tokens[i]))
            elif tokens[i]=="+":
                t.append(t[-2]+t[-1])
                t.pop(-2)
                t.pop(-2)
            elif tokens[i]=="*":
                t.append(t[-2]*t[-1])
                t.pop(-2)
                t.pop(-2)
            elif tokens[i]=="-":
                t.append(t[-2]-t[-1])
                t.pop(-2)
                t.pop(-2)
            else:
                t.append(int(t[-2]/t[-1]))
                t.pop(-2)
                t.pop(-2)
        return t[-1]