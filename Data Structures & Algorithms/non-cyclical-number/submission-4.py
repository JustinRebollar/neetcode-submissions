class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)

        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))

        return fast == 1

    def sumOfSquares(self, n: int) -> int:
            output = 0

            while n > 0:
                extractedDigit = n % 10
                output += extractedDigit ** 2
                n //= 10

            return output
