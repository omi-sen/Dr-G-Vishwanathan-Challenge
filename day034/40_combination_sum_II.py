class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        
        # 1. Sort the candidates to handle duplicates and enable pruning
        candidates.sort()
        
        def backtrack(start: int, current_target: int, path: list[int]):
            # Base Case: Target met
            if current_target == 0:
                ans.append(list(path))
                return
            
            # Explore decisions
            for i in range(start, len(candidates)):
                # Pruning: If the current number exceeds the remaining target, 
                # subsequent numbers will too (since the array is sorted).
                if candidates[i] > current_target:
                    break
                
                # Skip duplicate elements at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include the candidate and move to the next index
                path.append(candidates[i])
                backtrack(i + 1, current_target - candidates[i], path)
                
                # Backtrack (remove the element to try other paths)
                path.pop()
                
        backtrack(0, target, [])
        return ans
