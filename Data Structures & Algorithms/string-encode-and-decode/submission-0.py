DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
DELIMITER = "#"

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + DELIMITER + s

        return encoded


    def decode(self, s: str) -> List[str]:
        strs = []
        word_size = ""
        print(s)

        i = 0
        while i < len(s):
            char = s[i]
            print(f"character: '{s[i]}, word_size={word_size}'")
            if char in DIGITS:
                word_size += char
            elif char == DELIMITER and word_size != "":
                word_start = i + 1
                word_end = word_start + int(word_size)
                word = s[word_start:word_end]
                strs.append(word)
                i = word_end - 1
                word_size = ""
            else:
                word_size = ""

            i += 1

        return strs

