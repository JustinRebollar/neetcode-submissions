from collections import defaultdict

'''
zxyzxyz
-^^^
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        longest = 0
        left = 0

        for right, char in enumerate(s):
            count[char] += 1
            while count[char] > 1:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest