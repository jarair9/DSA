class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefixsum = [0] * len(nums)
        self.prefixsum[0] = nums[0]

        for i in range(1,len(nums)):
            self.prefixsum[i] = self.prefixsum[i-1] + nums[i]


    def update(self, index: int, val: int) -> None:
        
        self.index = index
        self.nums[index] = val

       
        if index == 0:
            self.prefixsum[0] = val
            index = 1
        for i in range(index, len(self.nums)):
            self.prefixsum[i] = self.prefixsum[i - 1] + self.nums[i]



    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixsum[right]

        return self.prefixsum[right] - self.prefixsum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)