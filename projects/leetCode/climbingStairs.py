# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# 1 -> 1
# 2 -> 2
# 3 -> 3
# 4 -> 5
# 5 -> 8

# [2,2,1]
# [1,2,2]
# [2,1,2]
# [1,1,1,1,1]
# [1,1,1,2]
# [1,1,2,1]
# [1,2,1,1]
# [2,1,1,1]

n = 38

numbers = [1,1]

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
    
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
        return(curr)

answer = Solution()

print(answer.climbStairs(n))