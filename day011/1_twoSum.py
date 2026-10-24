class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
 
        # A pair requires two different indices.
        if n < 2:
            return []
 
        value_to_index = {}
 
        for current in range(n):
            complement = target - nums[current]
 
            # Check before insertion so the current
            # index cannot be paired with itself.
            if complement in value_to_index:
                return [
                    value_to_index[complement],
                    current,
                ]
 
            # Save this value for elements that appear later.
            value_to_index[nums[current]] = current
 
        # No valid pair exists.
        return []