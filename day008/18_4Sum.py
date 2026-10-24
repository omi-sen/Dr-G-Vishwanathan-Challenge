class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        answer = []
 
        # Four different indices are required.
        if n < 4:
            return answer
 
        nums.sort()
 
        for first in range(n - 3):
            # Skip a repeated first value to avoid
            # generating duplicate quadruplets.
            if first > 0 and nums[first] == nums[first - 1]:
                continue
 
            for second in range(first + 1, n - 2):
                # Skip repeated second values only
                # within the current first value.
                if (
                    second > first + 1
                    and nums[second] == nums[second - 1]
                ):
                    continue
 
                left = second + 1
                right = n - 1
 
                while left < right:
                    current_sum = (
                        nums[first]
                        + nums[second]
                        + nums[left]
                        + nums[right]
                    )
 
                    # A smaller sum needs a larger left value.
                    if current_sum < target:
                        left += 1
 
                    # A larger sum needs a smaller right value.
                    elif current_sum > target:
                        right -= 1
 
                    else:
                        answer.append([
                            nums[first],
                            nums[second],
                            nums[left],
                            nums[right]
                        ])
 
                        left += 1
                        right -= 1
 
                        # Skip repeated boundary values
                        # to avoid duplicate answers.
                        while (
                            left < right
                            and nums[left] == nums[left - 1]
                        ):
                            left += 1
 
                        while (
                            left < right
                            and nums[right] == nums[right + 1]
                        ):
                            right -= 1
 
        return answer