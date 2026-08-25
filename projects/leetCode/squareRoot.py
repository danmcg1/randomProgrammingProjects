# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
#  The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

x = 2147395599

x = int(x)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        root = 0
        if x < 0:
            root = 0
        elif x == 1:
            root = 1 
        else:
            for n in range(1, x):
                if (n * n) <= x:
                    root = n
                elif (n * n) > x:
                    break
        return root

answer = Solution()

print(answer.mySqrt(x))