class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Build a clean string with only letters/numbers in lowercase
        cleaned = ""
        for char in s:
            if char.isalnum():  # checks if it's a letter or a number
                cleaned += char.lower()
                
        # Step 2: Check if the cleaned string equals its reverse
        return cleaned == cleaned[::-1]