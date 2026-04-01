class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        duplicate = False
        for num in nums:
            if num not in my_set:
                my_set.add(num)
            else:
                my_set.add(num)
                duplicate = True 
               

        return duplicate
        