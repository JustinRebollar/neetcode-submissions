class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = [0] * 26
        count_t = [0] * 26

        for char in s:
            position = ord('a') - ord(char)
            count_s[position] += 1

        for char in t:
            position = ord('a') - ord(char)
            count_t[position] += 1

        return count_s == count_t