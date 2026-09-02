class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        prefixsum = [0] * len(nums)

        for i in range(len(nums)):
            prefixsum[i] = sum(nums[:i]) + nums[i]

        return prefixsum

r = Solution()
print(r.runningSum([1,2,3,4]))