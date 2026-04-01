class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1
      

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m

            elif nums[m] > target:
                r =  r-1

            elif nums[m] < target:
                 l = m + 1
        return -1






        

        # I have an array of numbers sorted in ascending order [0,3,5,6,7,8,10]
        # Given integer is Target eg target = 8
        
        #Task: Create a function that searches for target within nums
        #       if Its exist return the index
        #              if it doesnt exist return -1
        #                   optimal solution 
