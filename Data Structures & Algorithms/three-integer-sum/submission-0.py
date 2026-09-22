class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]: #avoid duplicates
                continue
        # Step 2: Two pointers for the rest of the array
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                three_sum = a + nums[left] + nums[right]
                
                if three_sum > 0:
                    right -= 1  # Sum is too big, move right backward
                elif three_sum < 0:
                    left += 1   # Sum is too small, move left forward
                else:
                    # Found a valid triplet!
                    res.append([a, nums[left], nums[right]])
                    
                    # Move pointers and skip any duplicate numbers
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                        
        return res



        