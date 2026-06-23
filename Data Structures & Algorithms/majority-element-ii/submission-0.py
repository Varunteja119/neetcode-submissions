class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        arr=[]
        b=len(nums)
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        for i,n in d.items():
            if n>(b/3):
                arr.append(i)
        return arr