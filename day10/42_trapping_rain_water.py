class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        result = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    result += max_left - height[left]
                left += 1  # <-- Shifted left (now runs every time height[left] <= height[right])
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    result += max_right - height[right]
                right -= 1 # <-- Shifted left (now runs every time height[left] > height[right])

        return result
