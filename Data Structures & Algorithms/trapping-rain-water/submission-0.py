class Solution:
    def trap(self, height: List[int]) -> int:
        h=0
        w=0
        s=0
        e=len(height)-1
        while s<=e:
            if height[s]<height[e]:
                if h<height[s]:
                    w+=(height[s]-h)*(e-s+1)
                    h=height[s]
                w-=height[s]
                s+=1
            else:
                if h<height[e]:
                    w+=(height[e]-h)*(e-s+1)
                    h=height[e]
                w-=height[e]
                e-=1
        return w