from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for letter in word:
                freq[ ord(letter) - ord('a')] += 1
            key = tuple(freq)
            count[key].append(word)
        
        return list(count.values()) 