class PrefixTree:

    def __init__(self):
        self.preTree={}

    def insert(self, word: str) -> None:
        pointer=self.preTree
        for i in word:
            if i not in pointer:
                pointer[i]={}
            pointer=pointer[i]
        pointer["end"]=True

    def search(self, word: str) -> bool:
        pointer=self.preTree
        for i in word:
            if i not in pointer:
                return False
            pointer=pointer[i]
        if "end" in pointer:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        pointer=self.preTree
        for i in prefix:
            if i not in pointer:
                return False
            pointer=pointer[i]
        return True