class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        list1, list2 = zip(*sorted(zip(position, speed), reverse=True))
        list1, list2 = list(list1), list(list2)
        f=1
        s=(target-list1[0])/list2[0]
        for i in range(1,len(position)):
            if (target-list1[i])/list2[i]<=s:
                continue
            else:
                f+=1
                s=(target-list1[i])/list2[i]
        return f