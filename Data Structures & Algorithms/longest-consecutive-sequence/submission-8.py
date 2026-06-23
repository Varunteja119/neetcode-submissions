class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak=0
        s=set(nums)
        res=0
        if len(nums)==1:
            return 1
        for i in nums:
            curr=i
            while curr in s:
                streak+=1
                curr+=1
            res=max(res,streak)
            streak=0
        return res
            