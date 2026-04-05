class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # given array nums and int val
        # Remove all occurences of val in from nums IN PLACE
        #           in place: Means that the array should stay in place 

        # return the numa of remaming elements K tha do not contain val


        # Loop through nums 
        # check if num[i] != val
        # swap k w/ next i thats not k

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


        