from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            [1,2,4,6]
        --> [1,2,8,56]
            [42, 42,24,6] <--              
            [48,24,12,8]
        
        loop through nums 
            running --> + <--- running 
        '''

        res = []
        up = [1] * len(nums)

        for i in range(1, len(nums)):
            up[i] = up[i-1] * nums[i-1]
        down = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            up[i] *= down
            down *= nums[i]
        
        return up