class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        current = 0 
        while current <= right :
            if nums[current] == 0 : 
                nums[left] , nums[current] = nums[current] , nums[left]
                left = left + 1 
                current = current + 1
            elif nums[current] == 1 :
                current = current+1 
            else : 
                nums[right] , nums[current] = nums[current] , nums [right]
                right = right -1 