# 1588. Sum of All Odd Length Subarrays

# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
# Example 2:

# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
# Example 3:

# Input: arr = [10,11,12]
# Output: 66


class Solution:
    def sumOddLengthSubarrays(self, arr):
        total = 0

        # Choose every possible start index
        for start in range(len(arr)):

            # Choose every possible end index
            for end in range(start, len(arr)):

                # Length of current subarray
                length = end - start + 1

                # Only consider odd-length subarrays
                if length % 2 == 1:

                    # Add the sum of this subarray
                    total += sum(arr[start:end + 1])

        return total
        
r = Solution()
print(r.sumOddLengthSubarrays([1,4,2,5,3]))