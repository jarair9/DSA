

class Solution:
    def twosum(self, nums: list[int], target: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0
        right = len(nums) -1

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return [nums[left] , nums[right]]

            elif  total > target:
                right -= 1
            else:
                left += 1

        return []


r  = Solution()
print(r.twosum([1,2,4,8,5,6],9))


