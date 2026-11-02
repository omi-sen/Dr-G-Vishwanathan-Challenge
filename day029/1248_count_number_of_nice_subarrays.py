import collections

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # Tracks {odd_count_seen: frequency}
        count = collections.Counter({0: 1})
        current_odds = 0
        ans = 0
        
        for num in nums:
            # Increment if the current element is odd
            if num % 2 != 0:
                current_odds += 1
            
            # If (current_odds - k) exists in history, add its frequency to our answer
            ans += count[current_odds - k]
            
            # Record the current odds count state
            count[current_odds] += 1
            
        return ans
