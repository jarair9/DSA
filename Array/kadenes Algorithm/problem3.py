class Solution:
    def maximumProduct(self, nums: list[int]) -> int:

        max1 = float("-inf")
        max2 = float("-inf")
        max3 = float("-inf")

        min1 = float("inf")
        min2 = float("inf")

        for num in nums:

            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num

            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num

        product1 = max1 * max2 * max3

        product2 = min1 * min2 * max1

        return max(product1, product2)


r = Solution()
print(r.maximumProduct([1,2,3,4]))

# https://leetcode.com/problems/maximum-product-of-three-numbers/


