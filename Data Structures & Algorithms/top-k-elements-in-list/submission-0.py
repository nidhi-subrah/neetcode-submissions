class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        for i in range (len(nums)):
            count={}
            freq=[]
            for i in range(len(nums)+1):
                freq.append([])

            for n in nums:
                count[n]=count.get(n,0)+1

            for n,c in count.items(): #n is number, c is frequency count
                freq[c].append(n) #eg. numbers that appear 3 times go into bucket index 3
            res=[]
            for i in range(len(freq)-1, 0, -1):
                for n in freq[i]: #loops through specific freq. bucket
                    res.append(n) 
                    if len(res)==k:
                        return res
            

            

