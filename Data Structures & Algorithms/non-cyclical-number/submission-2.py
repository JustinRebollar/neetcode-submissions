class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def sumOfSquares(n: int) -> int:
            output = 0

            while n > 0:
                extractedDigit = n % 10
                output += extractedDigit * extractedDigit
                n //= 10

            return output

        while n not in visited:
            visited.add(n)
            n = sumOfSquares(n)

            if n == 1:
                return True

        return False
