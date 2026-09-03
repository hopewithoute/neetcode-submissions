class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n

        # 1. Bangun Prefix Cache (jalan dari kiri ke kanan)
        running_prefix = 1
        for i in range(n):
            prefix[i] = running_prefix
            running_prefix *= nums[i]

        # 2. Bangun Postfix Cache (jalan dari kanan ke kiri)
        running_postfix = 1
        for i in range(n - 1, -1, -1):
            postfix[i] = running_postfix
            running_postfix *= nums[i]

        # 3. Gabungkan kedua cache: prefix[i] * postfix[i]
        output = [0] * n
        for i in range(n):
            output[i] = prefix[i] * postfix[i]

        return output