class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def backTrack(i, subset):
            nonlocal res
            XOR = 0
            for num in subset:
                XOR ^= num 
            res += XOR

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backTrack(j+1, subset)
                subset.pop()

        backTrack(0, [])
        return res
        