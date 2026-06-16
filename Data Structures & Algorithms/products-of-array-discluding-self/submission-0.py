class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]*len(nums)
        r=[1]*len(nums)
        ls,rs=1,1
        for i in range(1,len(nums)):
            l[i]=nums[i-1]*ls
            ls*=nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            r[i]=nums[i+1]*rs
            rs=rs*nums[i+1]
        print (r)
        a=[]
        for i in range(len(l)):
            a.append(l[i]*r[i])
        return a


        