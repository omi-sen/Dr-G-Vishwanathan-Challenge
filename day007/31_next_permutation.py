class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
 
        # A single value cannot move to a different permutation.
        if n <= 1:
            return
 
        pivot = n - 2
 
        # Search for the rightmost position that can be increased.
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
 
        # A fully non-increasing array wraps around to the smallest permutation.
        if pivot < 0:
            nums.reverse()
            return
 
        successor = n - 1
 
        # Search from the right for the next larger value.
        while nums[successor] <= nums[pivot]:
            successor -= 1
 
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
 
        # Reverse the non-increasing suffix into the smallest possible order.
        nums[pivot + 1:] = reversed(nums[pivot + 1:])