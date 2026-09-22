from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        [1,2,2,3,3,3]
        freq = [] * len(nums)
        count = {}
        loop nums get the count of each number
        
        loop k, v counts 
        freq[k].append(v)

        loop through freq start top and loop till end 
        '''

        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(nums), 0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res