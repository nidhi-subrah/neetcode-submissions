class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)

        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix *= nums[i]
        
        postfix=1
        for i in range(len(nums)-1, -1, -1):
            res[i]*=postfix
            postfix*=nums[i]
        return res

        # total_product=1
        # output=[]
        # for i in nums:
        #     total_product *=i
        
        # for i in nums:
        #     current_product= total_product / i
        #     output.append(current_product)
        # return output
        