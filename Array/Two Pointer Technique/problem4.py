class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1

        for k in range(i,len(nums)):
            nums[k] = 0

        return nums
    
r = Solution()
print(r.moveZeroes([0,1,0,3,12]))