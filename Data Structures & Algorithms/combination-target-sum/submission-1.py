class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r=[]
        c=[]
        def back(s,re):
            if re==0:
                r.append(c.copy())
                return
            for i in range(s,len(nums)):
                if nums[i]>re:
                    continue
                c.append(nums[i])
                back(i,re-nums[i])
                c.pop()
        nums.sort()
        back(0,target)
        return r