class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Case 1: Target found
            if nums[mid] == target:
                return True
            
            # Case 2: Duplicates at the boundaries make it impossible to determine the sorted half
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            
            # Case 3: Left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Case 4: Right half is sorted
            else:
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False
