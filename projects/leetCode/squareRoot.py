# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
#  The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

x = 4

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        if x < 0:
            r = 0
        elif x == 1:
            r = 1
        else:
            r = x//2
            while r * r > x:
                r = (r + (x//r)) // 2 
        return r

answer = Solution()

print(answer.mySqrt(x))