class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Track the last seen index for each of the three characters
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        total_substrings = 0
        
        for i, char in enumerate(s):
            # Update the last seen position of the current character
            last_seen[char] = i
            
            # The number of valid substrings ending at index i is determined
            # by the smallest last-seen index among 'a', 'b', and 'c'
            total_substrings += min(last_seen.values()) + 1
            
        return total_substrings
