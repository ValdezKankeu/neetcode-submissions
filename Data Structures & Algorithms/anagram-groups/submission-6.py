from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        ["act","pots","tops","cat","stop","hat"]

        loop strs get the ord value of each number
        map[ordVal].append(word)

        '''
        count = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                freq[index] += 1
            count[tuple(freq)].append(word)
        return list(count.values())
         

