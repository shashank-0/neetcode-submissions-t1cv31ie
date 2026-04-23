class TimeMap:

    def __init__(self):
        self.s={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.s:
            self.s[key]=[[value,timestamp]]
        else:
            self.s[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.s and self.s[key][0][1]<=timestamp:
            i=0
            j=len(self.s[key])-1
            f=""
            while i<=j:
                m=(i+j)//2
                if timestamp>=self.s[key][m][1]:
                    f=self.s[key][m][0]
                    i=m+1
                else:
                    j=m-1
            return f
        else:
            return ""
