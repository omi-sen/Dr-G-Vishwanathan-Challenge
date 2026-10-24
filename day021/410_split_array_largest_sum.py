class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(max_sum: int) -> bool:
            # Greedily count the number of subarrays needed
            subarray_count = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > max_sum:
                    # Start a new subarray
                    subarray_count += 1
                    current_sum = num
                else:
                    current_sum += num
            
            # Returns true if we can split within the 'k' limit
            return subarray_count <= k

        # Define the bounds of our binary search space
        left = max(nums)   # Min possible maximum subarray sum
        right = sum(nums)  # Max possible maximum subarray sum
        result = right

        while left <= right:
            mid = left + (right - left) // 2
            
            if canSplit(mid):
                result = mid      # mid is a valid configuration; look for a smaller max sum
                right = mid - 1
            else:
                left = mid + 1    # mid is too small; increase the target max sum
                
        return result