class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # The problem asks for 1-indexed positions, so we add 1
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1   # We need a bigger sum, move left forward
            else:
                right -= 1  # We need a smaller sum, move right backward
        