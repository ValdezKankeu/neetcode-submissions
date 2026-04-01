class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                 return m

            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return l


#Im given an sorted array [-1,0,2,4,6,8]
# Given an target value = 4

        