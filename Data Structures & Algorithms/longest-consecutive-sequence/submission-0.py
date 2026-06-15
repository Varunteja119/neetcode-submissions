class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r=0
        s=set(nums)
        for i in nums:
            st,c=0,i
            while c in s:
                st+=1
                c+=1
            r=max(r,st)
        return r
        