class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s=set()
        l=0
        for i in range(len(nums)):
            if i-l>k:
                s.remove(nums[l])
                l+=1
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False

