class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atMost(target: int) -> int:
            if target < 0:
                return 0
            
            left = 0
            current_sum = 0
            count = 0
            
            for right in range(len(nums)):
                current_sum += nums[right]
                
                # Shrink window if current sum exceeds target limit
                while current_sum > target:
                    current_sum -= nums[left]
                    left += 1
                
                # The number of valid subarrays ending at 'right' is the window length
                count += (right - left + 1)
                
            return count

        return atMost(goal) - atMost(goal - 1)
