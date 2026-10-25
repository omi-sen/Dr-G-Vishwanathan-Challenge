class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Map to store the last seen index of each character
        char_map = {}
        left = 0
        max_length = 0
        
        # Iterate through the string with the right pointer
        for right, char in enumerate(s):
            # If the character is already in our map and its last seen index
            # is within or ahead of the current left boundary...
            if char in char_map and char_map[char] >= left:
                # Jump the left pointer directly past the previous occurrence
                left = char_map[char] + 1
            
            # Update the last seen index of the character
            char_map[char] = right
            
            # Calculate the current window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length
