class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        se=set()
        for i in nums:
            if i in se:
                return i
            se.add(i)
        return -1