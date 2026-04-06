class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = {}
        res, maxCount = 0,0

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
            res = num if counter[num] > maxCount else res
            maxCount = max(counter[num], maxCount )
        
        return res