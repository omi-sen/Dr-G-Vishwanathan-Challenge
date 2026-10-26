class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k
        
        # Total sum of all cards
        total_sum = sum(cardPoints)
        
        # If we take all cards, return total sum
        if k == n:
            return total_sum
        
        # Sum of the first window of size (n - k)
        current_window_sum = sum(cardPoints[:window_size])
        min_window_sum = current_window_sum
        
        # Slide the window across the array
        for i in range(window_size, n):
            # Add the new element entering the window, remove the one leaving
            current_window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, current_window_sum)
            
        # Maximum score is total sum minus the minimum subarray left behind
        return total_sum - min_window_sum
