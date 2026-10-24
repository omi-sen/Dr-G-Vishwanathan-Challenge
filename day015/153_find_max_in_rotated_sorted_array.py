class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        # Binary search loop
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost element,
            # it means the inflection point (and minimum) is in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum is in the left half (including mid itself).
            else:
                right = mid
                
        # When left == right, it points to the minimum element
        return nums[left]