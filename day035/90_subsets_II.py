class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Step 1: Sort to group duplicates
        
        def backtrack(start: int, path: list[int]):
            # Append a copy of the current valid subset
            res.append(list(path))
            
            for i in range(start, len(nums)):
                # Step 3: Skip duplicates at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Step 2: Make choice, recurse, and backtrack
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res
