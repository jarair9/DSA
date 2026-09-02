class NumArray:

    def __init__(self, nums):
    # Create a prefix sum array.
        self.prefixsum = [0] * len(nums)
    # The first prefix sum is simply the first number.
        self.prefixsum[0] = nums[0]
    # Now move from the second element to the end.
        for i in range(1,len(nums)):
            self.prefixsum[i] =  self.prefixsum[i-1] + nums[i]
            
    def sumRange(self, left: int, right: int) -> int:
        
        if left == 0:
            return self.prefixsum[right]

        return self.prefixsum[right] - self.prefixsum[left-1]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# 0
# 0+1
# 1+2