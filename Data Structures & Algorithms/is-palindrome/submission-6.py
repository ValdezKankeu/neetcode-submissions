class Solution:
    def isPalindrome(self, s: str) -> bool:
        newSting = ""
        for char in s:
            if char.isalnum():
                newSting += char.lower()
        
        l,r  = 0, len(newSting)-1
        while l <= r:
            if newSting[l] != newSting[r]:
                return False
            l += 1
            r -= 1
        
        return True