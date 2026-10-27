class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(index, current):
            if index == len(nums):
                result.append(current.copy())
                return
            current.append(nums[index])
            backtrack(index + 1, current)
            current.pop()
            backtrack(index + 1, current)
        backtrack(0, [])
        return result