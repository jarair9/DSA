
class Solution:
    def twosum(self, nums: list[int], target: int):

        hashmap = {}

        for index, num in enumerate(nums):
            constant = target - num

            if constant in hashmap:
                return [hashmap[constant], index]

            hashmap[index] = nums[index]
        return []
        




r  = Solution()
print(r.twosum([1,2,4,8,5],9))