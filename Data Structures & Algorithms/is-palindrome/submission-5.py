class Solution:
    def isPalindrome(self, s: str) -> bool:

        newString = ""
        for char in s:
            if char.isalnum():
                newString = newString + char.lower()

        l,r = 0, len(newString) -1
        
        while l < r:
            if newString[l] != newString[r]:
                return False
            l += 1
            r -= 1

        return True
        