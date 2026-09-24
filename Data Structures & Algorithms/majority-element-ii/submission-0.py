from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums) 
        res =[]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num in count:
            if count[num] > n/3:
                res.append(num)
        
        return res
            

        
        