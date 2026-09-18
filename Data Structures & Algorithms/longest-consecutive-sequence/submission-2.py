class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: Put everything into a set for instant lookups
        num_set = set(nums)
        longest = 0
        
        for n in num_set:
            # Step 2: Check if this number is the START of a sequence
            if (n - 1) not in num_set:
                # If it's a start, begin counting how long the streak goes
                length = 1
                while (n + length) in num_set:
                    length += 1
                
                # Keep track of the longest streak we've ever found
                longest = max(longest, length)
                
        return longest

        