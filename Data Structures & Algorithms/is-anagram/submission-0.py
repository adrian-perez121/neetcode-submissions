from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_1 = defaultdict(int)
        freq_2 = defaultdict(int)

        for c in s:
            freq_1[c] = freq_1[c] + 1
        for c in t:
            freq_2[c] = freq_2[c] + 1

        return freq_1 == freq_2 