class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        if n<3 : 
            return ans
        nums.sort()
        for fixed in range(n-2):
            if fixed > 0 and nums[fixed] == nums[fixed - 1] : 
                continue 
            left = fixed + 1
            right = n-1
            while (left < right ): 
                currSum = ( nums[fixed] + nums[left] + nums[right])
                if currSum < 0 :
                    left = left + 1
                elif currSum > 0 :
                    right = right - 1
                else: 
                    ans.append([nums[fixed], nums[left], nums[right]])
                    left = left + 1
                    right = right - 1

                    while left < right and nums[left] == nums[left-1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right+1]:
                        right = right -1

        return ans


