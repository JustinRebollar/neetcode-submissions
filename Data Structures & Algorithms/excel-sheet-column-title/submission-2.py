class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        print(abs(ord('A')))

        while columnNumber > 0:
            columnNumber -= 1
            temp = columnNumber % 26

            res.append(chr(ord('A') + temp))
            columnNumber //= 26

        return ''.join(reversed(res))