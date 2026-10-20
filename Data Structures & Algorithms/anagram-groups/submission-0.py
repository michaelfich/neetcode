from collections import defaultdict

class Solution:
    ALPHABET_COUNT = 26
    ORD_FIRST_LETTER = ord('a')

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            word_key = self._anagram_key(word)
            anagrams[word_key].append(word)

        result = []
        for _key, anagram_group in anagrams.items():
            result.append(anagram_group)

        return result

    def _anagram_key(self, word: str) -> tuple:
        count = [0] * self.ALPHABET_COUNT

        for w in word:
            ord_w = ord(w) - self.ORD_FIRST_LETTER
            count[ord_w] += 1

        return tuple(count)