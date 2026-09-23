class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        
        while left < right:
            # 1. Calculate width and height
            width = right - left
            current_height = min(heights[left], heights[right])
            
            # 2. Calculate area and update our max record
            current_area = width * current_height
            max_water = max(max_water, current_area)
            
            # 3. Move the pointer of the shorter wall inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
        