class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if its the same length
        # We need to create two maps
        # Keys = letter & Value = Occurence of letter 
        # loop thorugh a map and check is keys and value matches

        if len(s) != len(t):
            return False
        
        seenS, seenT = {}, {}

        for i in range(len(s)):
            seenS[s[i]] = 1 + seenS.get(s[i], 0)
            seenT[t[i]] = 1 + seenT.get(t[i], 0)
        
        for letter in seenS:
            if letter not in seenT or seenS[letter] > seenT[letter]:
                return False
            seenS[s[i]] = 1 - seenS.get(s[i], 0)

        return True
 
        
        
        