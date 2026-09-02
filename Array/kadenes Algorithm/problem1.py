class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = 0
        maxsum = float("-inf")


        for i in range(len(nums)):
            current += nums[i]
            maxsum = max(maxsum,current)

            if current < 0:
                current = 0

        return maxsum