class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        # Find the longest window that contains at most k zeros.
        left = 0
        count_zeros = 0
        best_ones = 0
        for right in range(len(nums)):
            
            if nums[right] == 0:
                count_zeros += 1
            
            while count_zeros > k:
                
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
              
                
            # Current window is valid
            best_ones = max(best_ones, right - left + 1)    

        return best_ones



        

r = Solution()
print(r.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))   
