class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = 0
        max_sub = nums[0]
        for n in nums : 
            if curr_sum < 0 :
                curr_sum = 0
            curr_sum += n
            max_sub = max(curr_sum , max_sub)
        return max_sub