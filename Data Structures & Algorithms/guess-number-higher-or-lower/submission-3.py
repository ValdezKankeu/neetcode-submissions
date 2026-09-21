# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l,r = 0, n
        
        while l <= r:
            myPick = (l+r) // 2
            pick = guess(myPick)

            if pick == 1:
                l = myPick + 1 
            elif pick == -1:
                r = myPick - 1
            else:
                return myPick