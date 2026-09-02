class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i - k - 1])
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False






# https://leetcode.com/problems/contains-duplicate-ii?envType=problem-list-v2&envId=sliding-window