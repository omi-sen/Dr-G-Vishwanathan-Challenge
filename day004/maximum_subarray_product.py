class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        global_max = nums[0]
        curr_max = nums[0]
        curr_min= nums[0]

        for n in nums[1:]: 
            temp_max = curr_max 
            curr_max = max (n , temp_max*n , curr_min*n)
            curr_min = min (n , temp_max * n , curr_min *n)

            global_max = max (curr_max , global_max)
        return global_max