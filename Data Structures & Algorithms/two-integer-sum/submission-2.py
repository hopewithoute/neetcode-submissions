class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums[i + 1:]:
                return [i, nums.index(complement, i + 1)]
        return []
