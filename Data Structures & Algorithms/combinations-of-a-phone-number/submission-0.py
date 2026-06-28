class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res=[]

        def back(i,sub):
            if i==len(digits):
                res.append(sub[:])
                return
            
            for j in keypad[digits[i]]:
                sub+=j
                back(i+1,sub)
                sub=sub[:-1]
        
        back(0,'')
        return res if res!=[''] else []