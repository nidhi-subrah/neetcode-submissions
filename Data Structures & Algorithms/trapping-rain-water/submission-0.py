class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0
        
        while left < right:
            # The side with the smaller max is our bottleneck
            if left_max < right_max:
                left += 1
                # Update our max seen so far on the left
                left_max = max(left_max, height[left])
                # Add the trapped water (if left_max is taller, it holds water)
                water += left_max - height[left]
            else:
                right -= 1
                # Update our max seen so far on the right
                right_max = max(right_max, height[right])
                # Add the trapped water
                water += right_max - height[right]
                
        return water