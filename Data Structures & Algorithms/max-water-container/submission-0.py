class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        re=0
        while l<r:
            h=min(heights[l],heights[r])
            w=r-l
            a=h*w
            re=max(a,re)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return re