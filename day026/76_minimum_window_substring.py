from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        # Dictionary to keep track of all the unique characters in t and their required counts.
        target_counts = Counter(t)
        
        # Dictionary to maintain the character frequencies of the current window.
        window_counts = {}
        
        # Number of unique characters in t that need to be present in the window.
        required = len(target_counts)
        
        # Number of unique characters in the current window that meet their target count in t.
        formed = 0
        
        # Result tuple: (window length, left pointer, right pointer)
        # Initialized with infinity and placeholder indices
        ans = (float("inf"), None, None)
        
        # Left pointer of the window
        left = 0
        
        # Move the right pointer to expand the window
        for right, char in enumerate(s):
            # Add the current character to the window tracking dictionary
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If the current character frequency matches its required frequency in t, 
            # increment our formed matches count.
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
            
            # Try and contract the window till the point where it ceases to be 'valid'.
            while left <= right and formed == required:
                # Update the result if this window is smaller than any previously found
                window_len = right - left + 1
                if window_len < ans[0]:
                    ans = (window_len, left, right)
                
                # The character at the left pointer is about to be removed from the window
                removed_char = s[left]
                window_counts[removed_char] -= 1
                
                # If removing this character breaks the valid criteria for the window,
                # decrement the formed count.
                if removed_char in target_counts and window_counts[removed_char] < target_counts[removed_char]:
                    formed -= 1
                
                # Move the left pointer forward to shrink the window
                left += 1
                
        # Return the minimum window substring if found, otherwise return an empty string
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
