class Solution:
    def isPalindrome(self, s: str) -> bool:

        newString = ""
        for char in s:
            if char.isalnum():
                newString = newString + char.lower()

        print(newString)
        print(newString[::-1] )
        return newString == newString[::-1] 
        