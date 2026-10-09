class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # stores indices of days
        
        for i, temp in enumerate(temperatures):
            # While stack has days with colder temps, resolve them
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
                
            stack.append(i)
            
        return result
        