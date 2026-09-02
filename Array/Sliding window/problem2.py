class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        window_sum = sum(nums[:k]) / k
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i-k]
            max_sum = max(window_sum,max_sum)

        return max_sum / k

r = Solution()
print(r.findMaxAverage([1,12,-5,-6,50,3],4))