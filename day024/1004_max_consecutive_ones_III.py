class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        max_length = 0
        zero_count = 0
        
        # Expand the window using the right pointer
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                
            # If zeros exceed k, contract the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
                
            # Update the maximum valid window size found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length
