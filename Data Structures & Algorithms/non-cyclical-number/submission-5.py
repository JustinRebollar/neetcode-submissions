class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)

        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))

        return slow == 1

    def sumOfSquares(self, n: int):
        res = 0

        while n:
            res += (n % 10) ** 2
            n //= 10

        return res