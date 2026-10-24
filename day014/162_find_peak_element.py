class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If we are on an upward slope, peak is to the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # If we are on a downward slope, peak is at mid or to the left
            else:
                right = mid
                
        # left and right will converge to the peak element index
        return left
