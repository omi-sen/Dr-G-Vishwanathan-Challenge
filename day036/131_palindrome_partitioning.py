class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        current_path = []
        
        def is_palindrome(sub_str: str) -> bool:
            # Check if a substring reads the same forward and backward
            return sub_str == sub_str[::-1]
            
        def dfs(start_idx: int):
            # Base Case: If we've reached the end of the string, record the path
            if start_idx == len(s):
                result.append(list(current_path))
                return
            
            # Explore every possible cut from start_idx to the end of the string
            for end_idx in range(start_idx, len(s)):
                substring = s[start_idx : end_idx + 1]
                
                # Only proceed if the current substring is a palindrome
                if is_palindrome(substring):
                    current_path.append(substring)  # Choose
                    dfs(end_idx + 1)                # Explore the rest
                    current_path.pop()              # Backtrack (Undo Choose)

        dfs(0)
        return result
