class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = {0: 1}  # base case: prefix sum 0 occurs once

        for num in nums:
            current_sum += num
            
            # Check if there is a prefix sum that equals (current_sum - k)
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
                
            # Update the frequency of the current prefix sum
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count
