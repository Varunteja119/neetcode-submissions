
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []
        c = []
        def back():
            if len(c) == len(nums):
                r.append(c.copy())
                return
            for i in range(len(nums)):
                if nums[i] in c:
                    continue
                c.append(nums[i])
                back()
                c.pop()
        back()
        return r
