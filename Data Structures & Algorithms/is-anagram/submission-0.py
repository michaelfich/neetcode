from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return self.letter_frequency(s) == self.letter_frequency(t)

    def letter_frequency(self, word: str) -> dict:
        freq = defaultdict(int)

        for c in word:
            freq[c] += 1

        return freq
