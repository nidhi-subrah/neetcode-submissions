class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping: #closing bracket
                if stack:
                    top_element = stack.pop() #If valid, will be opening
                else:
                    top_element = "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

        