# Removing element from array
# return the number k
# remove the nums in place


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        i = 0
        for j in range(1,len(nums)):
            if nums[i] != val: 
            # when this executes but the below will not executed that executes when that is equal
                i += 1
                nums[i] = nums[j]
        return i


        