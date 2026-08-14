class Solution:
    def isHappy(self, n: int) -> bool:
        numbersSeen = []

        while True:
            tempSum = 0
            for integer in list(str(n)):
                tempSum += int(integer) * int(integer)

            #print(integer, tempSum, numbersSeen)
            
            if tempSum == 1:
                return True
            elif (tempSum in numbersSeen):
                return False

            n = tempSum
            numbersSeen.append(tempSum)


        return False