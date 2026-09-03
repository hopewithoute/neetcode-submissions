class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n

        # Pass 1: Simpan prefix product langsung ke output array
        running_prefix = 1
        for i in range(n):
            output[i] = running_prefix
            running_prefix *= nums[i]

        # Pass 2: Kalikan dengan postfix product secara on-the-fly
        running_postfix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= running_postfix
            running_postfix *= nums[i]

        return output