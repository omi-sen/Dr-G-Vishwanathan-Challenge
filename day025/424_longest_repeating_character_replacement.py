class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        
        for right in range(len(s)):
            # Add the current character to our window frequency tracker
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Keep track of the most frequent character seen in any valid window configuration
            max_freq = max(max_freq, count[s[right]])
            
            # Current window size is (right - left + 1)
            # The number of characters to replace is (window_size - max_freq)
            # If this exceeds k, the window is invalid, so shift the left pointer
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
        # The maximum window size achieved will be the total length minus the final left pointer
        return len(s) - left
