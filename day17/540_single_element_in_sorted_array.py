class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # We use strict less-than because when left == right, 
        # we have narrowed down to the single unique element.
        while left < right:
            mid = (left + right) // 2
            
            # If mid is even, mid ^ 1 checks mid + 1
            # If mid is odd, mid ^ 1 checks mid - 1
            if nums[mid] == nums[mid ^ 1]:
                # We are in the left half before the single element.
                # The single element must be on the right side.
                left = mid + 1
            else:
                # We are in the right half after the single element.
                # The single element is at mid or to its left.
                right = mid
                
        return nums[left]
