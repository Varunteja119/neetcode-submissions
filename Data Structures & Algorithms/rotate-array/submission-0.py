class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        a=len(nums)-1
        k=k%n
        while k:
            temp=nums[a]
            for i in range(a,0,-1):
                nums[i]=nums[i-1]
            nums[0]=temp
            k-=1


