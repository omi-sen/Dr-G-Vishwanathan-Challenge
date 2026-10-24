import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Define the search space for the eating speed 'k'
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            # Calculate total hours needed with current speed 'mid'
            total_hours = 0
            for pile in piles:
                # math.ceil(pile / mid) calculates hours for the current pile
                total_hours += math.ceil(pile / mid)
            
            # If Koko can finish within h hours, try a slower speed
            if total_hours <= h:
                right = mid
            # If she takes too long, she needs to eat faster
            else:
                left = mid + 1
                
        return left
